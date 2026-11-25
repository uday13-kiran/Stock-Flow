
from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.models.user import User


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_organization(db: Session, name: str):
    organization = Organization(name=name)

    db.add(organization)
    db.commit()
    db.refresh(organization)

    return organization


def create_user(
    db: Session,
    email: str,
    password_hash: str,
    organization_id: int
):
    user = User(
        email=email,
        password_hash=password_hash,
        organization_id=organization_id
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
