FROM python:3.12-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=1

COPY app/src/requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

RUN apt-get update \
    && apt-get install -y curl \
    && curl -o /usr/src/app/wait-for-it.sh \
    https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh \
    && chmod +x /usr/src/app/wait-for-it.sh

