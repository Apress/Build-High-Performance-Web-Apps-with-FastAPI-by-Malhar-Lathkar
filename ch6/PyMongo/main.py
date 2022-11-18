from pymongo import MongoClient
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List

DB = "mydata"
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
    client=MongoClient()
    DB = "mydata"
    coll = "books"
    bc=client[DB][coll]
    yield bc
    
@app.get("/books", response_model=List[Book])
def get_books(bc=Depends(get_collection)):
    """Get all books in list form."""
    books=list(bc.find())
    return books



@app.get("/books/{id}", response_model=Book)
def get_book(id: int, bc=Depends(get_collection)):
    """Get book for the specified ID."""
    b1=bc.find_one({"bookID": id})
    return b1


@app.post("/books")
def add_book(b1: Book, bc=Depends(get_collection)):
    """Add new book."""
    result = bc.insert_one(b1.dict())
    return "Book added successfully"
##Try to write the PUT and DELETE operation functions
