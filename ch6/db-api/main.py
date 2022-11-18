from fastapi import FastAPI, Depends
from pydantic import BaseModel
import sqlite3
from typing import List

def init_db():
    conn=sqlite3.connect("mydata.sqlite3")
    cur=conn.cursor()
    qry='''
    SELECT count(name) FROM sqlite_master WHERE type='table'
    AND name='Books'
    '''
    cur.execute(qry)

    if cur.fetchone()[0]==0:
        qry='''
        CREATE TABLE IF NOT EXISTS Books (
        id  INTEGER (10) PRIMARY KEY,
        title STRING (50),
        author STRING (20),
        price INTEGER (10),
        publisher STRING (20)
        );
        '''
    
        cur.execute(qry)
    conn.close()

init_db()

app=FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: int
    publisher: str

def get_cursor():
    conn=sqlite3.connect("mydata.sqlite3")
    conn.row_factory = sqlite3.Row
    cur=conn.cursor()
    yield (conn,cur)

@app.post("/books")
def add_book(book: Book, db=Depends(get_cursor)):
    id=book.id
    title=book.title
    author=book.author
    price=book.price
    publisher=book.publisher
    cur=db[1]
    conn=db[0]
    ins="INSERT INTO books VALUES (?,?,?,?,?)"
    cur.execute(ins,(id,title,author,price,publisher))
    conn.commit()
    return "Record successfully added"

@app.get("/books")
def get_books(db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    
    cur.execute("select * from Books;")
    books=cur.fetchall()
    return books

@app.get("/books/{id}")
def get_book(id: int, db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    
    cur.execute("select * from Books where id=?",(id,))
    book=cur.fetchone()
    #result = [dict(row) for row in books]
    return book
from fastapi import Body

@app.put("/books/{id}")
def update_book(id:int, pub:str=Body(), db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    qry="UPDATE Books set publisher=? where id=?"

    cur.execute(qry,(pub, id) )
    conn.commit()
    return "Book updated successfully"

@app.delete("/books/{id}")
def del_book(id:int, db=Depends(get_cursor)):
    cur=db[1]
    conn=db[0]
    
    cur.execute("delete from Books where id=?",(id,))
    conn.commit()
    return "Book deleted successfully"
    
            

    

    

