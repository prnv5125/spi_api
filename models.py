from sqlalchemy import Column, Integer, String, TIMESTAMP
from .database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(String, nullable=True)
    url = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
