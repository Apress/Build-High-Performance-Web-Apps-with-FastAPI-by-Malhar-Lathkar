from fastapi import FastAPI
app = FastAPI()

@app.get("/employee/{name}")
async def get_employee(name:str, age:int):
    return {"name":name, "age":age}
