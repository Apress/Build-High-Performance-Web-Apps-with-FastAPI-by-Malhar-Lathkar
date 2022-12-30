from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
SQLALCHEMY_DATABASE_URL = "sqlite:///./mydata.sqlite3"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

from sqlalchemy.orm import sessionmaker, Session
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from sqlalchemy import Column, Integer, String
class Books(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    price = Column(Integer)
Base.metadata.create_all(bind=engine)

from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    price:int

    class Config:
        orm_mode = True

from fastapi import FastAPI, Depends, Body
from typing import List

app=FastAPI()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.post('/books', response_model=Book)
def add_book(b1: Book, db: Session = Depends(get_db)):
    bkORM=Books(**b1.dict())
    db.add(bkORM)
    db.commit()
    db.refresh(bkORM)
    return b1

@app.get('/books', response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    recs = db.query(Books).all()
    return recs

@app.get('/books/{id}', response_model=Book)
def get_book(id:int, db: Session = Depends(get_db)):
    return db.query(Books).filter(Books.id == id).first()


@app.put('/books/{id}', response_model=Book)
def update_book(id:int, price:int=Body(), db: Session = Depends(get_db)):
    bkORM = db.query(Books).filter(Books.id == id).first()
    bkORM.price=price
    db.commit()
    return db.query(Books).filter(Books.id == id).first()

@app.delete('/books/{id}')
def del_book(id:int, db: Session = Depends(get_db)):
    try:
        db.query(Books).filter(Books.id == id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    return "book deleted successfully"