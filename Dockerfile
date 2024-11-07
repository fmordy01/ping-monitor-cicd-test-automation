FROM python:3.11.2-slim

WORKDIR /app

COPY . /app


#install dependencies
RUN pip install -r requirements.txt