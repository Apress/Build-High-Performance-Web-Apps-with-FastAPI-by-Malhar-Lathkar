from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

class Student(BaseModel):
    StudentID:int
    name:str
    subjects:Dict[str, int]

app=FastAPI()

@app.post("/student")
async def addnew(student:Student):
    return student
