from fastapi import FastAPI
import uvicorn

app=FastAPI()

#restful规范:

@app.get("/",
         tags=["这是一个get测试接口"],
         summary="这是summary",
         description="这是description",
         response_description="这是响应解释"
        )
async def get():
    return {"get方法"}

@app.delete("/")
async def delete():
    return {"delete方法"}

@app.post("/")
async def post():
    return{"post方法"}

@app.put("/")
async def put():
    return{"put方法"}

if __name__=="__main__":
    uvicorn.run("fastapi_test2:app",port=7600,reload=True)