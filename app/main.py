from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE id = %s", (item_id,))
    item = cur.fetchone()
    cur.close()
    conn.close()
    return {"item": item}
