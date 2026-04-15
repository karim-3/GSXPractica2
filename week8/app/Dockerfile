FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app

USER appuser

CMD ["python", "app.py"]