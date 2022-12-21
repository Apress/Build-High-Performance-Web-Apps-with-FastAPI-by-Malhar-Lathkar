from fastapi import FastAPI, WebSocket
import random
app = FastAPI()
@app.websocket("/test")
async def test(websocket: WebSocket):
    await websocket.accept()
    while True:
        request = await websocket.receive_text()
        print(request)
        while True:
            i=random.randint(1,1000)
            await websocket.send_text(str(i))
            if i==100:
                break
