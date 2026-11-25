from pydantic import BaseModel

from app.schemas.product import ProductResponse


class DashboardResponse(BaseModel):
    total_products: int
    total_quantity: int
    low_stock_count: int
    low_stock_products: list[ProductResponse]