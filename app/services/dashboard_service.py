from sqlalchemy.orm import Session

from app.repositories import dashboard_repository


def get_dashboard(db: Session, organization_id: int):
    total_products = dashboard_repository.get_total_products(
        db, organization_id
    )

    total_quantity = dashboard_repository.get_total_quantity(
        db, organization_id
    )

    low_stock_products = dashboard_repository.get_low_stock_products(
        db, organization_id
    )

    return {
        "total_products": total_products,
        "total_quantity": total_quantity,
        "low_stock_count": len(low_stock_products),
        "low_stock_products": low_stock_products
    }