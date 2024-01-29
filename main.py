from fastapi import FastAPI
from fastapi.responses import JSONResponse
from apps.products import router as productRouter
from apps.orders import router as orderRouter

app = FastAPI()

app.include_router(productRouter, prefix="/products")
app.include_router(orderRouter, prefix="/orders")
