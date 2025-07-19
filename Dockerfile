FROM python:3.10-slim


# ✅ Install Node.js 18 safely
RUN apt update && apt install -y wget gnupg && \
    wget -qO- https://deb.nodesource.com/setup_18.x | bash - && \
    apt install -y nodejs

RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y

RUN mkdir /app/
COPY . /app
WORKDIR /app
RUN pip3 install pip && pip3 install --upgrade pip && pip3 install -U -r requirements.txt
# Optional: explicitly define these, if needed during build
ENV API_ID=${API_ID}
ENV API_HASH=${API_HASH}
ENV SESSION_STRING=${SESSION_STRING}

CMD python3 main.py
