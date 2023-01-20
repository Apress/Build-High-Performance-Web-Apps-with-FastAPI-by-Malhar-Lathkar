from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
template = Jinja2Templates(directory="templates")
 
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("hello.html", {"request": request})
