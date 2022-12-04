from fastapi import FastAPI

books=FastAPI()

#routes for books API
@books.get("/books")
async def get_books():
    return "pass"
#define rest of the path operation functions here
