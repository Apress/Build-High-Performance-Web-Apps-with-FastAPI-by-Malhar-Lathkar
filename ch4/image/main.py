from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

app=FastAPI()

@app.get("/img/", response_class=HTMLResponse)
async def showimg(request:Request):    
    return template.TemplateResponse("static-img.html",
                                     {"request":request})

