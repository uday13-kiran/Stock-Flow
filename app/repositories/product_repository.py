from sqlalchemy.orm import Session

from app.models.product import Product


def create_product(db: Session, product_data: dict):
    product = Product(**product_data)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_products(db: Session, organization_id: int):
    return db.query(Product).filter(
        Product.organization_id == organization_id
    ).all()


def get_product_by_id(
    db: Session,
    product_id: int,
    organization_id: int
):
    return db.query(Product).filter(
        Product.id == product_id,
        Product.organization_id == organization_id
    ).first()


def update_product(db: Session, product, update_data: dict):
    for key, value in update_data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product):
    db.delete(product)
    db.commit()

    return True


def get_product_by_sku(db: Session, sku: str, organization_id: int):
    return db.query(Product).filter(
        Product.sku == sku,
        Product.organization_id == organization_id
    ).first()