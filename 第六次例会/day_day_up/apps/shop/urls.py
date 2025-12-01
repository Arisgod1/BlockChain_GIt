from fastapi import APIRouter

shop=APIRouter()

@shop.get("/items")
async def get_items():
    return{"items":"prices"}

@shop.get("/stores")
async def get_stores():
    return{"stores":"numbers"}
