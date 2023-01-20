from fastapi import FastAPI, Path, Query
app = FastAPI()
@app.get("/employee/{name}/branch/{branch_id}")
async def get_employee(name:str, brname:str,
                       branch_id:int=Path(1, gt=0, le=100),
                       age:int=Query(None, ge=20, lt=61)):
    employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
    return employee
