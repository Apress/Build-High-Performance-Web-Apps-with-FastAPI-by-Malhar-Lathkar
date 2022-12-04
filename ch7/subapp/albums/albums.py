from fastapi import FastAPI
albums=FastAPI()

#routes for albums API
@albums.get("/albums")
async def get_albums():
    return "pass"
#define rest of the path operation functions here
