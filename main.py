
from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import organization, user, product
from app.routes.auth_routes import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="StockFlow Inventory MVP")

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "StockFlow API is running"}
