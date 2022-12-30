from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

names = [{"A01": "Alice"}, {"B01": "Bob"}, {"C01" : "Christie"}]

class MyException(Exception):
    def __init__(self, msg:str):
        self.msg=msg

@app.exception_handler(MyException)
async def myexceptionhanlder(request:Request, e:MyException):
    return JSONResponse(status_code=406, content={"message": "{} was encountered".format(e)})


@app.get("/names/{id}")
async def get_name(id: str):
    for name in names:
        if id in name.keys():
            return {"name": name[id]}
    else:
        if id=='end':
            raise MyException(id)
        else:
            raise HTTPException(status_code=404, detail="Name not found")