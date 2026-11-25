from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    sku: str
    description: str | None = None
    quantity: int = 0
    cost_price: float | None = None
    selling_price: float | None = None
    low_stock_threshold: int = 5


class ProductUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    description: str | None = None
    quantity: int | None = None
    cost_price: float | None = None
    selling_price: float | None = None
    low_stock_threshold: int | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    sku: str
    description: str | None
    quantity: int
    cost_price: float | None
    selling_price: float | None
    low_stock_threshold: int
    organization_id: int

    model_config = {"from_attributes": True}