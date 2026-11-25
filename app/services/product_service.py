from sqlalchemy.orm import Session

from app.repositories import product_repository


def create_product(db: Session, data, organization_id: int):
    existing_product = product_repository.get_product_by_sku(
        db, data.sku, organization_id
    )

    if existing_product:
        raise ValueError("SKU already exists in your organization")

    product_data = data.model_dump()
    product_data["organization_id"] = organization_id

    return product_repository.create_product(db, product_data)


def get_products(db: Session, organization_id: int):
    return product_repository.get_products(db, organization_id)


def get_product(db: Session, product_id: int, organization_id: int):
    product = product_repository.get_product_by_id(
        db, product_id, organization_id
    )

    if not product:
        raise ValueError("Product not found")

    return product


def update_product(
    db: Session,
    product_id: int,
    data,
    organization_id: int
):
    product = product_repository.get_product_by_id(
        db, product_id, organization_id
    )

    if not product:
        raise ValueError("Product not found")

    update_data = data.model_dump(exclude_unset=True)

    if "sku" in update_data:
        existing_product = product_repository.get_product_by_sku(
            db, update_data["sku"], organization_id
        )

        if existing_product and existing_product.id != product.id:
            raise ValueError("SKU already exists in your organization")

    if "quantity" in update_data and update_data["quantity"] < 0:
        raise ValueError("Quantity cannot be negative")

    if (
        "low_stock_threshold" in update_data
        and update_data["low_stock_threshold"] < 0
    ):
        raise ValueError("Threshold cannot be negative")

    return product_repository.update_product(
        db, product, update_data
    )


def delete_product(db: Session, product_id: int, organization_id: int):
    product = product_repository.get_product_by_id(
        db, product_id, organization_id
    )

    if not product:
        raise ValueError("Product not found")

    return product_repository.delete_product(db, product)