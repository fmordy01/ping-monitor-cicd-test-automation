FROM python:3.11.2-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "ping_service.py"]



