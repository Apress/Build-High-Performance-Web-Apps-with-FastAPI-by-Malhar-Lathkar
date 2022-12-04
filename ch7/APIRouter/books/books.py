from fastapi import APIRouter

from .models import book

books = APIRouter(prefix="/books",
                   tags=["books"])


#routes for books API
@books.get("/")
async def get_books():
    return "pass"
@books.get("/{id}")
async def get_book(id:int):
    return "pass"
@books.post("/")
async def add_book(b1:book):
    return "pass"
@books.put("/{id}")
async def update_book(id:int):
    return "pass"
@books.delete("/{id}")
async def del_book(id:int):
    return "pass"
