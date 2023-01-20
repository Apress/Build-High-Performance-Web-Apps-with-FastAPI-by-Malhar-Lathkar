from dataclasses import dataclass
@dataclass
class Product:
    prodId:int
    prodName:str
    price:float
    stock:int
p1=Product(1, "Ceiling Fan", 2000, 50)
print (p1)
