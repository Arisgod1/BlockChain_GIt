import asyncio
from tortoise import Tortoise
from tortoise_orm.settings import TORTOISE_ORM

async def init():
    # 初始化Tortoise
    await Tortoise.init(config=TORTOISE_ORM)
    
    # 生成数据库表结构
    await Tortoise.generate_schemas()
    
    print("数据库表结构创建完成!")
    
    # 关闭连接
    await Tortoise.close_connections()

if __name__ == "__main__":
    asyncio.run(init())