from fastapi import FastAPI, Request

from src.auth.routers import router as auth_router
from src.basket.routers import router as basket_router
from src.purchase.routers import router as purchase_router

app = FastAPI(
    title="Online shop",
    description=("Online shop with basket"),
    version="0.0.1"
)

app.include_router(auth_router)
app.include_router(basket_router)
app.include_router(purchase_router)