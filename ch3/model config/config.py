from pydantic import BaseModel

class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int

    class Config:
        schema_extra = {
            "example": {
                "prodId": 1,
                "prodName": "Ceiling Fan",
                "price": 2000,
                "stock": 50
            }
        }
