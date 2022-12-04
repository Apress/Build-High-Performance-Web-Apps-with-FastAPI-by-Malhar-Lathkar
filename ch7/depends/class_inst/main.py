from fastapi import Depends, FastAPI

app = FastAPI()

persons=[
  {"name": "Tom", "age": 20},
  {"name": "Mark", "age": 25},
  {"name": "Pam", "age": 27}
]

employees=[
  {"name": "Tom", "salary": 20000},
  {"name": "Mark", "salary": 25000},
  {"name": "Pam", "salary": 27000}
]
##async def properties(x: int, y: int):
##    return {"from": x, "to": y}
class properties:
    def __call__(self, x:int, y:int):
        self.x=x
        self.y=y
        return self
##    def __call__(self):
##        return self
        
@app.get("/persons/")
async def get_persons(params: properties = Depends(properties())):
    return persons[params.x:params.y]

@app.get("/employees/")
async def get_employees(params: properties = Depends(properties())):
    return employees[params.x:params.y]
