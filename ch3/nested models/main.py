from pydantic import BaseModel, SecretStr, HttpUrl, Json

from pydantic import BaseModel

class Suppliers(BaseModel):
    supplierID:int
    supplierName:str

from typing import List   
 
class Products(BaseModel):
    productID:int
    productName:str
    price:int
    suppler:List[Suppliers]

class Customers(BaseModel):
    custID:int
    custName:str
    products:List[Products]

from fastapi import FastAPI

app = FastAPI()    

@app.post("/customer")
async def getcustomer(c1:Customers):
    return c1


