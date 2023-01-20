from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
template = Jinja2Templates(directory="templates")
 
app = FastAPI()

@app.get("/employee/{name}/{salary}",response_class=HTMLResponse)
async def employee(request:Request, name:str, salary:int):
    data= {"name":name, "salary":salary}
    return template.TemplateResponse("employee.html", {"request": request, "data":data})
