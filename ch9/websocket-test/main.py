from fastapi import FastAPI

from fastapi.websockets import WebSocket

app = FastAPI()


@app.websocket("/wstest")
async def wstest(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "From WebSocket Server"})
    await websocket.close()



