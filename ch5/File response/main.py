from fastapi import FastAPI
from fastapi.responses import FileResponse

file="wildlife.mp4"
app=
fastAPI()
@app.get("/", response_class=FileResponse)
async def index():
    return file
