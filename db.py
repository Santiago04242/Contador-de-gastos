import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

try:
    motor = psycopg2.connect(
        host="localhost",
        database=os.getenv("DATABASE"),
        user="postgres",
        password=os.getenv("PASSWORD"),
        port= "5432"
    )
except Exception as e:
    print("Error al conectar a la base de datos:", e)

if __name__ == "__main__":
    cursor = motor.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS gastos (id SERIAL PRIMARY KEY, descripcion TEXT, monto FLOAT, categoria TEXT, fecha DATE NOT NULL DEFAULT CURRENT_DATE);")
    motor.commit()
