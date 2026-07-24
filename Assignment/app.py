from fastapi import FastAPI
from routes.product_route import router

app=FastAPI()

app.include_router(router)