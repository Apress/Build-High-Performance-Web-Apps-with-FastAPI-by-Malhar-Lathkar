from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    price: int

books=[{"title":"Python", "price":500}, {"title":"FastAPI", "price":750}]

app=FastAPI()

@app.get("/list/{id}")
async def list(id:int):
    return books[id-1]

@app.post("/list", status_code=201)
async def addnew(b1:Book):
    books.append(b1.dict())
    return b1