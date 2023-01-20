from fastapi import FastAPI, Path, Query
from typing import Optional
app = FastAPI()

@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(branch_id:int,name:str=Path(None, min_length=10), brname:str=Query(None, min_length=5, max_length=10), age:Optional[int]=None):
    employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
    return employee
