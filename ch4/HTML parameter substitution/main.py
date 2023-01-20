from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/{name}", response_class=HTMLResponse)
async def index(name):
    ret='''
<html>
<body>
<h2 style="text-align: center;">Hello {}!</h2>
</body>
</html>
'''.format(name)
    return HTMLResponse(content=ret)
