from fastapi import Depends, FastAPI

app = FastAPI()

persons=[
  {"name": "Tom", "age": 20},
  {"name": "Mark", "age": 25},
  {"name": "Pam", "age": 27}
]


async def properties(x: int, y: int):
    return {"from": x, "to": y}

        
@app.get("/persons/")
async def get_persons(params: dict = Depends(properties)):
    return persons[params['from']:params['to']]
