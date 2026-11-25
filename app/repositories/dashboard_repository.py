from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.product import Product


def get_total_products(db: Session, organization_id: int):
    return db.query(func.count(Product.id)).filter(
        Product.organization_id == organization_id
    ).scalar()


def get_total_quantity(db: Session, organization_id: int):
    return db.query(func.coalesce(func.sum(Product.quantity), 0)).filter(
        Product.organization_id == organization_id
    ).scalar()


def get_low_stock_products(db: Session, organization_id: int):
    return db.query(Product).filter(
        Product.organization_id == organization_id,
        Product.quantity <= Product.low_stock_threshold
    ).all()