from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        product_id=product.product_id,
        name=product.name,
        price=product.price,
        url=product.url,
        created_at=datetime.utcnow()
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.product_id == product_id).first()
