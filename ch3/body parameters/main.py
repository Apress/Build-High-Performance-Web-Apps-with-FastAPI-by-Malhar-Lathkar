from fastapi import FastAPI, Body, Request

app = FastAPI()

@app.post("/product")
async def addnew(request: Request, prodId:int = Body(), prodName:str = Body(), price:float=Body(), stock:int = Body()):
    product={'Product ID':prodId, 'product name':prodName,
             'Price':price, 'Stock':stock}
    return product
