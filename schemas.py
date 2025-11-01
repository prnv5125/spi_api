from pydantic import BaseModel
from datetime import datetime

class ProductBase(BaseModel):
    product_id: int
    name: str
    price: str | None = None
    url: str

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
