from fastapi import FastAPI, Depends
from pydantic import BaseModel
import aiosqlite
import asyncio
from typing import List


app=FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: int
    publisher: str

async def get_cursor():
    conn=await aiosqlite.connect("mydata.sqlite3")
    conn.row_factory = aiosqlite.Row
    cur=await conn.cursor()
    yield (conn,cur)

@app.post("/books")
async def add_book(book: Book, db=Depends(get_cursor)):
    id=book.id
    title=book.title
    author=book.author
    price=book.price
    publisher=book.publisher
    cur=db[1]
    conn=db[0]
    ins="INSERT INTO books VALUES (?,?,?,?,?)"
    await cur.execute(ins,(id,title,author,price,publisher))
    await conn.commit()
    return "Record successfully added"
##
@app.get("/books")
async def get_books(db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    
    await cur.execute("select * from Books;")
    books=await cur.fetchall()
    return books
##
@app.get("/books/{id}")
async def get_book(id: int, db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    
    await cur.execute("select * from Books where id=?",(id,))
    book=await cur.fetchone()
    return book
from fastapi import Body

@app.put("/books/{id}")
def update_book(id:int, pub:str=Body(), db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    qry="UPDATE Books set publisher=? where id=?"

    await cur.execute(qry,(pub, id) )
    await conn.commit()
    return "Book updated successfully"
##
@app.delete("/books/{id}")
def del_book(id:int, db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    
    await cur.execute("delete from Books where id=?",(id,))
    await conn.commit()
    return "Book deleted successfully"
    
            

    

    

