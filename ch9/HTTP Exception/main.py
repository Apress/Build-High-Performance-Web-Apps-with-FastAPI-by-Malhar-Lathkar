from fastapi import FastAPI, HTTPException

app = FastAPI()

names = [{"A01": "Alice"}, {"B01": "Bob"}, {"C01" : "Christie"}]


@app.get("/names/{id}")
async def get_name(id: str):
    for name in names:
        if id in name.keys():
            return {"name": name[id]}
    else:
        raise HTTPException(status_code=404, detail="Name not found")