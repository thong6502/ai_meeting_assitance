from transformers import pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import torch
import gradio as gr

# Load environment variables from .env file
load_dotenv()

# Set the device for torch
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print(f"Using device: {device}")


def remove_non_ascii(text):
    """
    Removes all characters outside the ASCII range from a given text.
    This ensures compatibility with systems or models that only process ASCII characters.
    """
    return ''.join(i for i in text if ord(i) < 128)

#######------------- LLM and Chains-------------#######

# Initialize the language model
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

# Chain 1: Corrects financial terminology in the transcript
correction_template = """
You are an intelligent assistant specializing in financial products. Your task is to process a transcript and correct financial terms.

- Spell out full terms for acronyms (e.g., 'HSA' to 'Health Savings Account (HSA)').
- Convert spoken numbers for products to numeric form (e.g., 'five two nine' to '529 (Education Savings Plan)').
- Use context to disambiguate terms (e.g., 'LTV' as 'Loan to Value' or 'Lifetime Value').
- Leave other numbers or metrics as they are (e.g., 'twenty three percent').

Produce only the adjusted transcript.

Original Transcript:
{transcript}

Adjusted Transcript:
"""
correction_prompt = ChatPromptTemplate.from_template(correction_template)
correction_chain = correction_prompt | llm | StrOutputParser()

# Chain 2: Generates meeting minutes from the corrected transcript
minutes_template = """
Generate meeting minutes and a list of tasks based on the provided context.

Context:
{context}

Meeting Minutes:
- Key points discussed
- Decisions made

Task List:
- Actionable items with assignees and deadlines
"""
minutes_prompt = ChatPromptTemplate.from_template(minutes_template)

# Final combined chain
final_chain = (
    {"context": correction_chain}
    | minutes_prompt
    | llm
    | StrOutputParser()
)

#######------------- Speech-to-Text and Processing Pipeline-------------#######

def transcript_audio(audio_file):
    """
    Transcribes the audio, corrects terminology, and generates meeting minutes.
    """
    transcriber = pipeline(
        task="automatic-speech-recognition",
        model="openai/whisper-base",
        chunk_length_s=30,
        stride_length_s=(4, 2),
        device=device,
    )

    # Transcribe audio and clean the transcript
    raw_transcript = transcriber(audio_file, batch_size=1)["text"]
    ascii_transcript = remove_non_ascii(raw_transcript)

    # Invoke the processing chain
    result = final_chain.invoke({"transcript": ascii_transcript})

    # Save the result to a file
    output_file = "meeting_minutes_and_tasks.txt"
    with open(output_file, "w") as file:
        file.write(result)

    return result, output_file

#######------------- Gradio Interface-------------#######

audio_input = gr.Audio(sources="upload", type="filepath", label="Upload your audio file")
output_text = gr.Textbox(label="Meeting Minutes and Tasks")
download_file = gr.File(label="Download Generated Minutes and Tasks")

iface = gr.Interface(
    fn=transcript_audio,
    inputs=audio_input,
    outputs=[output_text, download_file],
    title="AI Meeting Assistant",
    description="Upload a meeting audio file. The tool will transcribe, correct financial terms, and generate meeting minutes with a task list."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7000)
