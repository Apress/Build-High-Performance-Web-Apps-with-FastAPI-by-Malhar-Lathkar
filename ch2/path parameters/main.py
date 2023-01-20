From fastapi import FastAPI

app = FastAPI()

@app.get("/employee/{name}/{age}")
async def user(name:str, age:int):
    return {"name":name, "age":age}
