from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/employee/{name}")
async def get_employee(name:str, age:Optional[int]=None):
    return {"name":name, "age":age}

app = FastAPI()

