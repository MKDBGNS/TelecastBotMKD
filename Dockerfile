FROM python:3.10-slim

RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs

RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y

RUN mkdir /app/
COPY . /app
WORKDIR /app
RUN pip3 install pip && pip3 install --upgrade pip && pip3 install -U -r requirements.txt

CMD python3 main.py
