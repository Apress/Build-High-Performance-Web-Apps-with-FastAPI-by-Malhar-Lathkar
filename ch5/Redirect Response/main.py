from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import Response, RedirectResponse
from fastapi.templating import Jinja2Templates

template = Jinja2Templates(directory="templates")
 
app = FastAPI()
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return RedirectResponse("/redirect")
    return template.TemplateResponse("form.html",
                                     {"request": request})
