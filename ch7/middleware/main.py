from fastapi import FastAPI, Request, Header
from typing import Optional
app = FastAPI()


@app.middleware("http")
async def add_header(request: Request, call_next):
    print ("Message by Middleware before operation function")
    response = await call_next(request)
    response.headers["X-Framework"] = "FastAPI"
    return response

@app.get("/")
async def index(X_Framework: Optional[str] = Header(None)):
    return {"message":"Hello World"}
