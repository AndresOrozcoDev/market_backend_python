from pydantic import BaseModel, Field
from typing import Optional

class Response(BaseModel):
    message: str
    data: list

class Supermarket(BaseModel):
    name: str

class Category(BaseModel):
    name: str

class Product(BaseModel):
    name: str
    value: int
    unit: str
    supermarket_name: str
    category_name: str