from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

scheme = HTTPBasic()


""" @app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(scheme)):
    return {"username": credentials.username, "password": credentials.password} """
@app.get("/")
def index(logininfo: HTTPBasicCredentials = Depends(scheme)):
    return {"message": "Hello {}".logininfo.username}