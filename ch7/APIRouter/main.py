from fastapi import FastAPI
from books import books
from albums import albums

app = FastAPI()

app.include_router(books.books)
app.include_router(albums.albums)

@app.get("/")
async def root():
    return {"message": "Home page"}
