FROM python:3.9.4-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "auth:app","--host", "0.0.0.0", "--port", "80"] 