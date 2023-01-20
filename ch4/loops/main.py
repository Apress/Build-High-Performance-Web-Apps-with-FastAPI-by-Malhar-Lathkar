from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
template = Jinja2Templates(directory="templates")
 
app = FastAPI()

@app.get("/profile/", response_class=HTMLResponse)
async def info(request:Request):
    data={"name":"Ronie", "langs":["Python", "Java", "PHP", "Swift", "Ruby"]}
    return template.TemplateResponse("profile.html",
                                   {"request":request, "data":data})
