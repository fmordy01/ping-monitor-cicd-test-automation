FROM python:3.11.2-slim

#Installing ping utility 
RUN apt-get update && apt-get install -y iputils-ping && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app


#install dependencies
RUN pip install -r requirements.txt