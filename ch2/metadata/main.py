from fastapi import FastAPI, Path, Query
app = FastAPI()
@app.get("/employee/{EmpName}/branch/{branch_id}")
async def get_employee(branch_id:int, brname:str,
                       name:str=Path(None,
                                     title='Name of Employee',
                                     description='Length not more than 10 chars',
                                     alias='EmpName',max_length=10),
                       age:int=Query(None,include_in_schema=False)):
    employee={'name':name, 'Branch':brname, 'Branch ID':branch_id, 'age':age}
    return employee
