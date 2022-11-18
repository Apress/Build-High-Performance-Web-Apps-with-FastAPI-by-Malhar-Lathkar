from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI, Depends, Body
from pydantic import BaseModel

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./mydata.sqlite3"

metadata = sqlalchemy.MetaData()

booklist = sqlalchemy.Table(
    "booklist",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("author", sqlalchemy.String),
    sqlalchemy.Column("price", sqlalchemy.Integer),
    sqlalchemy.Column("publisher", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class Book(BaseModel):
    id: int
    title: str
    author:str
    price:int
    publisher: str


app = FastAPI()

async def get_db():
    db = databases.Database(DATABASE_URL)
    await db.connect()
    yield db

##@app.on_event("startup")
##async def startup():
##    await database.connect()
##
##
##@app.on_event("shutdown")
##async def shutdown():
##    await database.disconnect()


@app.get("/books", response_model=List[Book])
async def get_books(db=Depends(get_db)):
    query = booklist.select()
    return await db.fetch_all(query)


@app.post("/books/", response_model=Book)
async def add_book(b1: Book, db=Depends(get_db)):
    query = booklist.insert().values(id=b1.id, title=b1.title,
                                     author=b1.author,
                                     price=b1.price, publisher=b1.publisher)
    await db.execute(query)
    return "Book added successfully"

@app.get("/books/{id}")
async def get_book(id: int, db=Depends(get_db)):
    query=booklist.select().where(booklist.c.id==id)    
    return await db.fetch_one(query)

@app.put("/books/{id}")
async def update_book(id:int, new_price:int=Body(), db=Depends(get_db)):
    query=booklist.update().where(booklist.c.id==id).values(price=new_price)
    

    await db.execute(query)
    return "Book updated successfully"

@app.delete("/books/{id}")
async def del_book(id:int, db=Depends(get_db)):
    query=booklist.delete().where(booklist.c.id==id)
    

    await db.execute(query)
    return "Book deleted successfully"
