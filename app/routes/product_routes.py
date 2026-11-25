from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services import product_service
from app.models.user import User


router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=ProductResponse, status_code=201)
def create_product(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return product_service.create_product(
            db, data, current_user.organization_id
        )

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return product_service.get_products(
        db, current_user.organization_id
    )


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return product_service.get_product(
            db, product_id, current_user.organization_id
        )

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        return product_service.update_product(
            db, product_id, data, current_user.organization_id
        )

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        product_service.delete_product(
            db, product_id, current_user.organization_id
        )

        return {"message": "Product deleted successfully"}

    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))