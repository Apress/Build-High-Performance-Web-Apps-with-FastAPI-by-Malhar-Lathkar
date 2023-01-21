from fastapi import FastAPI
from fastapi.responses import StreamingResponse
app=FastAPI()
async def generator():
    for i in range(1,11):
        yield "Line {}\n".format(i)


@app.get("/")
async def main():
    return StreamingResponse(generator())
file="large_file.txt"
@app.get("/")
def index():
    def readfile():  
        with open(file, mode="rb") as f:   
            yield from f   

    return StreamingResponse(readfile(), media_type="text/plain")

