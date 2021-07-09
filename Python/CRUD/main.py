from fastapi import FastAPI
from pydantic import BaseModel
import json
import sqlite3

app= FastAPI (debug=True)

with open('variable.json')as f:
    books=json.load(f)

@app.get('/tessst')
async def get_books():
    return books


class item (BaseModel):
    kursi : str
    kondisi:str

@app.post("/cobapost")
async def create_item(item:item):
    return books 

def fetch_stock_data(id: int):

    conn = sqlite3.connect('DataKondisiKursi.db')
    c = conn.cursor()
    sql=("SELECT * FROM variable")

  
@app.get("/")
def read_root():
    return {"Hello": "World"}


