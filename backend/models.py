from sqlalchemy import Column, Integer, String, Float
from .database import Base
from pydantic import BaseModel

# SQLAlchemy Model
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    price = Column(Float)
    image = Column(String)
    description = Column(String)
    quantity = Column(Integer, default=0)

# Pydantic Schema
class ProductSchema(BaseModel):
    id: int
    name: str
    category: str
    price: float
    image: str
    description: str
    quantity: int = 0

    class Config:
        from_attributes = True




    
