from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello World"}

@app.get("/{name}/{id}")
async def user(name:str, id:int):
    return {"name":name, "id":id}
