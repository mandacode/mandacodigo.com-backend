FROM python:3.12-slim

WORKDIR /var/www/app

ENV PYTHONUNBUFFERED=1

COPY app/src/requirements.txt .

RUN pip install -r requirements.txt

RUN pip install wait-for-it

COPY app/ .
