from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/testjs/{name}", response_class=HTMLResponse)
async def jsdemo(request:Request, name:str):    
    data={"name":name}
    return template.TemplateResponse("static-js.html",
                                   {"request":request, "data":data})
