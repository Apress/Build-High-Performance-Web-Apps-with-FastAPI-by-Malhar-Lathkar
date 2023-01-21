from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
template = Jinja2Templates(directory="templates")
 
app = FastAPI()
from fastapi import Cookie

@app.get("/", response_class=HTMLResponse)
async def index(request: Request, user:str = Cookie(None)):
    return template.TemplateResponse("form.html",
                                     {"request": request, "user":user})

from fastapi.responses import Response

@app.post("/setcookie/")
async def setcookie(request:Request, response: Response,
                    user:str=Form(...), pwd:str=Form(...)):
    response.set_cookie(key="user", value=user)
    return {"message":"Hello World"}



@app.get("/readcookie/")
async def read_cookie(user: str = Cookie(None)):
    return {"username": user}
