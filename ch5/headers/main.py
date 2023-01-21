from fastapi import FastAPI
app=FastAPI()
@app.get("/header/")
async def set_header():
    content = {"message": "Hello World"}
    headers = {"X-Web-Framework": "FastAPI", "Content-Language": "en-US"}

from typing import Optional
from fastapi import Header
@app.get("/read_header/")
async def read_header(accept_language: Optional[str] = Header(None)):
    return {"Language": accept_language}
