from fastapi import FastAPI
import datetime

app = FastAPI()

@app.on_event("startup")
def startup_event():
    print('Server started\n')
    log= open("log.txt", mode="a")
    log.write("Application startup at {}\n".format(datetime.datetime.now()))
    log.close()

@app.on_event("shutdown")
async def shutdown_event():
    print('server Shutdown :', datetime.datetime.now())
    log= open("log.txt", mode="a")
    log.write("Application shutdown at {}\n".format(datetime.datetime.now()))
    log.close()
