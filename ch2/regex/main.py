from fastapi import FastAPI, Path, Query
from typing import Optional
app = FastAPI()

@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(branch_id:int, brname:str, age:int,
                       name:str=Path(None, regex="^[J]|[h]$")):
    employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
    return employee

