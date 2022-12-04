from fastapi import FastAPI, Request, Depends
from fastapi.responses import Response
app = FastAPI()

@app.get("/")
async def index(request:Request, response: Response):
    response.set_cookie(key="user", value="admin")
    response.set_cookie(key="api_key", value="abcdef12345")
    return {"message":"Home Page"}

def credentials(request):
    dct=request.cookies
    try:
        return dct['api_key']
    except:
        return None

persons=[
  {"name": "Tom", "age": 20},
  {"name": "Mark", "age": 25},
  {"name": "Pam", "age": 27}
]    
    
@app.get("/persons/")
async def get_persons(key=Depends(credentials(Request))):
    if key==None:
        return {"message":"API key not validated"}
    else:
        return persons
