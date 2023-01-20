from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
async def index():
    ret='''
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
'''
    return Response(content=ret, media_type="text/html")
