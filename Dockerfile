FROM python:3.10-slim

# Install system deps
RUN apt update && apt install -y ffmpeg wget gnupg

# Install Node.js
RUN wget -qO- https://deb.nodesource.com/setup_18.x | bash - && apt install -y nodejs

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install Python deps
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Railway injects env vars automatically
# Start bot
CMD ["python3", "main.py"]
