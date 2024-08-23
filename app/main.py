from fastapi import FastAPI
from typing import Optional
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
    cur.execute("SELECT DISTINCT city FROM fallen_soldiers")
    cities = cur.fetchall()
    cur.close()
    conn.close()
    
    return templates.TemplateResponse("home.html", {"request": request, "cities": [city[0] for city in cities]})

@app.get("/table", response_class=HTMLResponse)
async def read_table(request: Request):
    conn = psycopg2.connect(
        host="34.71.236.251",
        dbname="mydb",
        user="user",
        password="password",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name, age, city, description FROM fallen_soldiers")
    #cur.execute("SELECT * FROM fallen_soldiers")
    rows = cur.fetchall()
    headers = ["שם", "גיל", "עיר", "תיאור","id"]#[desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    
    return templates.TemplateResponse("table.html", {"request": request, "headers": headers, "rows": rows})


@app.get("/search", response_class=HTMLResponse)
def search(request: Request, city: Optional[str] = None, name: Optional[str] = None):
    query = "SELECT name, age, city, description FROM fallen_soldiers WHERE 1=1"
    params = []

    if name:
        query += " AND name ILIKE %s"
        params.append(f"%{name}%")

    if city:
        query += " AND city = %s"
        params.append(city)

    conn = psycopg2.connect(
        host="34.71.236.251",
        dbname="mydb",
        user="user",
        password="password",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    headers = ["שם", "גיל", "עיר", "תיאור"]
    cur.close()
    conn.close()

    return templates.TemplateResponse("table.html", {"request": request, "headers": headers, "rows": rows})
@app.get("/health")
async def health_check():
    return {"status": "ok"}