from pydantic import BaseModel, Field
from typing import Optional

class Response(BaseModel):
    message: str
    data: list

class Supermarket(BaseModel):
    name: str = Field(max_length=50)