from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int
    Inventory_val:float

class ProductVal(BaseModel):
    prodId:int
    prodName:str
    Inventory_val:float
##
app = FastAPI()
@app.post("/product/", response_model=ProductVal)
async def addnew(product:Product):
    product.Inventory_val=product.price*product.stock
    return product


