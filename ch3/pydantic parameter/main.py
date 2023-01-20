from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int
  
app = FastAPI()
@app.post("/product/")
async def addnew(product:Product):
    return product
