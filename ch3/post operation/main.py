from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int
  
app = FastAPI()

productlist=[]

@app.post("/product/")
async def addnew(product:Product):
    productlist.append(product)
    return productlist

