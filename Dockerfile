FROM python:3.10-slim

# Cài đặt các gói hệ thống cần thiết
RUN apt-get update && apt-get install -y ffmpeg git && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép requirements và cài đặt dependencies Python
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container, ngoại trừ .venv
COPY . .

# Expose port cho Gradio
EXPOSE 7000

# Chạy ứng dụng Gradio
CMD ["python", "speechToText_app.py"] 