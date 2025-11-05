FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias de la API y PostgreSQL
RUN pip install fastapi uvicorn psycopg2-binary

COPY server.py /app/server.py

EXPOSE 8000

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
