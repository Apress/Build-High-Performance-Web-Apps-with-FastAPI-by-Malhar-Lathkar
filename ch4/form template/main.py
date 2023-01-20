from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

app=FastAPI()

from fastapi import Form

@app.post("/form/")
async def getform(name:str=Form(...), add:str=Form(...), Post:str=Form(...)):
    return {"Name":name, "Address":add, "Post Applied":Post}


