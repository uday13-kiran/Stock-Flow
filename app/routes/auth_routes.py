
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.auth import SignupRequest, LoginRequest, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup")
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    try:
        user = auth_service.signup(
            db,
            data.email,
            data.password,
            data.organization_name
        )

        return {
            "message": "Account created successfully",
            "user_id": user.id,
            "organization_id": user.organization_id
        }

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        token = auth_service.login(
            db,
            data.email,
            data.password
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except ValueError as error:
        raise HTTPException(status_code=401, detail=str(error))
