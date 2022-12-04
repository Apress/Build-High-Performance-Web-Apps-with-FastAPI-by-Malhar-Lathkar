from fastapi import FastAPI, Depends

app = FastAPI()

def dow():
    from datetime import datetime
    dow=datetime.now().weekday()
    return dow

@app.get("/")
async def root(day=Depends(dow)):
    if day==6:
        return {"message": "Service not available on Sunday"}
    return {"message": "Home page"}


