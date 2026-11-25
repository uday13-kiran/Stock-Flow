from fastapi import FastAPI

from app.core.database import Base, engine
from app.models import Organization, User, Product

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="StockFlow Inventory MVP")


@app.get("/")
def home():
    return {"message": "StockFlow API is running"}
