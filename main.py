from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine
from app.models import organization, user, product

from app.routes.auth_routes import router as auth_router
from app.routes.product_routes import router as product_router
from app.routes.dashboard_route import router as dashboard_router  


Base.metadata.create_all(bind=engine)

app = FastAPI(title="StockFlow Inventory MVP")

app.add_middleware(
CORSMiddleware,
allow_origins=[
"http://localhost:5173",
"https://stock-flow-frontend-blush.vercel.app"
],
allow_credentials=True,
allow_methods=[""],
allow_headers=[""],
)

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {"message": "StockFlow API is running"}
