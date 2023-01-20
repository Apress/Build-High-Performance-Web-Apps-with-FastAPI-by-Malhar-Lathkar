from fastapi import FastAPI
from pydantic import BaseModel, SecretStr, HttpUrl, Json
from typing import Dict

class Employee(BaseModel):
    ID: str
    pwd: SecretStr
    salary: int
    details: Json     
    FBProfile: HttpUrl

app=FastAPI()

@app.post("/employee")
async def addnew(emp:Employee):
    return emp
