from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import psycopg2
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/", response_class=HTMLResponse)
async def read_table(request: Request):
    conn = psycopg2.connect(
        host="34.71.236.251",
        dbname="mydb",
        user="user",
        password="password",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM fallen_soldiers")
    rows = cur.fetchall()
    headers = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    
    return templates.TemplateResponse("table.html", {"request": request, "headers": headers, "rows": rows})


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

@app.get("/health")
async def health_check():
    return {"status": "ok"}