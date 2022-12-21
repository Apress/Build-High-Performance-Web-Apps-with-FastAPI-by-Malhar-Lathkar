from fastapi import FastAPI,  Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

from fastapi.staticfiles import StaticFiles


app = FastAPI()


#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def hello(request: Request):
    file=open("templates/socket.html")
    html=file.read()
    #print (html)
    #return templates.TemplateResponse("socket.html", {"request": request})
    return HTMLResponse(html)

from fastapi import WebSocket
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
