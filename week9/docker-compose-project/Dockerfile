FROM python:3.11-slim

# Instal·lem dependències del sistema i curl
RUN apt-get update && apt-get install -y curl gcc libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instal·lem el driver de la base de dades
RUN pip install psycopg2-binary

COPY app.py .

# Seguretat: usuari no-root [cite: 220]
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app
USER appuser

CMD ["python", "app.py"]