from fastapi import FastAPI
from albums import albums
from books import books

app = FastAPI()


@app.get("/stores")
async def root():
    return {"message": "Home page"}

app.mount("/albumapi", albums.albums)
app.mount("/bookapi", books.books)
