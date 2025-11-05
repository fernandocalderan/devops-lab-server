from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        host="database",
        user="usuario",
        password="clave",
        dbname="ejemplo"
    )

@app.get("/")
def home():
    return {"status": "API en funcionamiento"}

@app.get("/usuarios")
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 'Hola desde PostgreSQL'")
    result = cur.fetchone()
    conn.close()
    return {"respuesta": result[0]}
