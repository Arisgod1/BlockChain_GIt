#例如:当不同业务模块（如商品、购物车、支付）由不同的团队开发时,我们就需要将路由分离开，并定义不同的前缀。

from fastapi import FastAPI
import uvicorn
from apps.shop.urls import shop
from apps.user.urls import user
app=FastAPI()  #全局实例化

app.include_router(shop,prefix="/shop",tags=["购物中心接口"])
app.include_router(user,prefix="/user",tags=["用户中心接口"])

if __name__=="__main__":
    uvicorn.run("main:app",port=8000,reload=True)
