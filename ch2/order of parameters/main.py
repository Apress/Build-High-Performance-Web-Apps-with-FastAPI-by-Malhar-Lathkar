from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(name:str, brname:str, branch_id:int,
                       age:Optional[int]=None):
    employee={'name':name, 'Branch':brname,
              'Branch ID':branch_id, 'age':age}
    return employee


