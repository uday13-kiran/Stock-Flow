
from sqlalchemy.orm import Session

from app.repositories import auth_repository
from app.core.security import hash_password, verify_password, create_access_token


def signup(db: Session, email: str, password: str, organization_name: str):
    existing_user = auth_repository.get_user_by_email(db, email)

    if existing_user:
        raise ValueError("Email already registered")

    organization = auth_repository.create_organization(
        db, organization_name
    )

    hashed_password = hash_password(password)

    user = auth_repository.create_user(
        db,
        email,
        hashed_password,
        organization.id
    )

    return user


def login(db: Session, email: str, password: str):
    user = auth_repository.get_user_by_email(db, email)

    if not user:
        raise ValueError("Invalid email or password")

    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid email or password")

    token = create_access_token(user.id)

    return token
