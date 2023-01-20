from pydantic import BaseModel

from pydantic import BaseModel
class Product(BaseModel):
    prodId:int
    prodName:str
    price:float
    stock:int
    class Config:
        orm_mode=True

from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductORM(Base):
    __tablename__ = 'products'
    prodId = Column(Integer, primary_key=True, nullable=False)
    prodName = Column(String(63), unique=True)
    price = Column(Float)
    stock = Column(Integer)

prod_alchemy = ProductORM(
    prodId=1,
    prodName='Ceiling Fan',
    price=2000,
    stock=50
)

product = Product.from_orm(prod_alchemy)

product=Product(prodId=2, prodName='LED Bulb', price=250, stock=50)
prod_alchemy=ProductORM(**product.dict())

