from fastapi import APIRouter

user=APIRouter()

@user.post("/login")
async def user_login():
    return {"user":"login"}

@user.post("/register")
async def user_register():
    return {"user":"register"}

