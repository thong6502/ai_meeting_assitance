# AI Meeting Assistant

## Overview
This project is an **AI-powered meeting assistant** that automatically transcribes meeting audio, corrects financial terminology, and generates structured meeting minutes and actionable task lists. It leverages state-of-the-art technologies such as **Whisper (speech-to-text)**, **Gradio (user interface)**, and **large language models (LLMs)** to deliver accurate, organized, and insightful meeting documentation.

## Features
- Upload an audio file of your meeting.
- Automatic speech recognition and transcription using Whisper.
- Correction of financial terms and acronyms for clarity and accuracy.
- Generation of meeting minutes and a list of actionable tasks.
- Simple, user-friendly web interface powered by Gradio.
- Downloadable results as a text file.

## Example Output
```
Here are the meeting minutes and a list of tasks based on the provided context:

---

**Meeting Minutes**

**Date:** [Insert Date of Meeting - e.g., October 26, 2023]
**Attendees:** [Implied: Leadership Team, Stakeholders, Finance, Strategy]
**Subject:** Quarterly Business Update & Strategic Outlook

**Key Points Discussed:**
- Risk Management & Capital Health: ...
- Financial Forecast (Coming Quarter): ...
- Strategic Initiatives: ...
- Shareholder Confidence: ...

**Decisions Made:**
- No new explicit decisions were stated in this update. ...

---

**Task List**
- Task 1: Ongoing Risk Monitoring & Management ...
- Task 2: Drive Revenue Growth from Key Solutions ...
- Task 3: Finalize Pay Plus IPO Preparations ...
- Task 4: Develop Post-IPO Growth Strategies ...
- Task 5: Prepare Q3 Shareholder Communication ...
```

## Installation
### 1. Local Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd AI_meeting_assistance
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
4. **Run the app:**
   ```bash
   python speechToText_app.py
   ```
5. **Access the interface:**
   Open your browser and go to [http://localhost:7000](http://localhost:7000)

### 2. Using Docker
1. **Build the Docker image:**
   ```bash
   docker build -t ai-meeting-assistant .
   ```
2. **Run the container:**
   ```bash
   docker run -p 7000:7000 ai-meeting-assistant
   ```
3. **Access the interface:**
   Open your browser and go to [http://localhost:7000](http://localhost:7000)

> **Note:** The `.dockerignore` file ensures that your local `.venv` folder is not copied into the Docker image.

## Dependencies
- Python 3.10+
- [transformers](https://pypi.org/project/transformers/)
- [torch](https://pypi.org/project/torch/)
- [gradio](https://pypi.org/project/gradio/)
- [pydantic](https://pypi.org/project/pydantic/)
- [langchain](https://pypi.org/project/langchain/)
- [langchain-community](https://pypi.org/project/langchain-community/)
- [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- System: ffmpeg, git (auto-installed in Docker)

## File Structure
- `speechToText_app.py` — Main application file
- `requirements.txt` — Python dependencies
- `Dockerfile` — For containerized deployment
- `.dockerignore` — Excludes `.venv` from Docker image
- `meeting_minutes_and_tasks.txt` — Example output

## Usage
1. Upload your meeting audio file (WAV, MP3, etc.) via the Gradio interface.
2. The app will transcribe, correct, and summarize the meeting.
3. Download the generated meeting minutes and task list as a text file.

## Acknowledgements
- Hugging Face Transformers & Whisper
- Gradio
- LangChain
- Google Generative AI 