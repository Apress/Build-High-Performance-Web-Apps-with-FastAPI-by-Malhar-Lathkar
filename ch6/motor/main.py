#from pymongo import MongoClient
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List
import motor.motor_asyncio

DB = "mydb"
coll = "books"


# Book class defined in Pydantic
class Book(BaseModel):
    bookID: int
    title: str
    author:str
    price:int
    publisher: str


# Instantiate the FastAPI
app = FastAPI()

def get_collection():
    client=motor.motor_asyncio.AsyncIOMotorClient()
    DB = "mydb"
    coll = "books"
    bc=client[DB][coll]
    yield bc
    
@app.get("/books", response_model=List[Book])
async def get_books(bc=Depends(get_collection)):
    """Get all books in list form."""
    books=await bc.find().to_list(1000)
    return books



@app.get("/books/{id}", response_model=Book)
async def get_book(id: int, bc=Depends(get_collection)):
    b1=await bc.find_one({"bookID": id})
    return b1



@app.post("/books")
async def add_book(b1: Book, bc=Depends(get_collection)):
    result = await bc.insert_one(b1.dict())
    return "Book added successfully"

##Try to add PUT and DELETE operations
