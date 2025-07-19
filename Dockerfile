# Use lightweight Python base
FROM python:3.10-slim

# 🛠 Install system dependencies
RUN apt update && \
    apt install -y ffmpeg wget gnupg && \
    apt clean

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs


# 📁 Set working directory
WORKDIR /app

# 📦 Copy project files
COPY . .

# 🐍 Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 🟢 Railway injects env vars at runtime — no need to declare them here

# 🚀 Start bot
CMD ["python3", "main.py"]
