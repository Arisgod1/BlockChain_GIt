import uvicorn  # 导入 uvicorn 库，它是一个高性能的 ASGI 服务器，用于运行 FastAPI 应用
from fastapi import FastAPI  # 导入 FastAPI 类，它是构建 API 应用的核心

# 创建 FastAPI 应用程序的实例
# 这个实例（app）将是定义所有 API 路由、处理请求和配置应用的中心对象。
app = FastAPI()


# @app.get("/") 是一个装饰器，用于定义一个路由（或叫端点）。
# 它指定：当客户端使用 HTTP GET 方法请求根路径 "/" 时，执行下面定义的函数。
# async 是 Python 中定义异步函数（Asynchronous function）的关键字。
# 异步函数在处理 I/O 密集型任务（如等待网络请求、数据库查询）时，
# 可以暂停当前任务，去处理其他任务，从而提高并发性能。
@app.get("/")
async def user_info():
    # 当客户端访问 / 路径时，此函数会被调用并返回一个 Python 字典。
    # FastAPI 会自动将这个字典转换为 JSON 格式的 HTTP 响应体，
    # 并自动设置响应状态码（默认为 200 OK）和必要的响应头（如 Content-Type: application/json）。
    return {"name": "cai", "age": "19"}

# 定义另一个路由：当客户端使用 HTTP GET 方法请求 /hello 路径时，执行此函数。
@app.get("/hello")
async def hello():
    # 返回一个 Python 集合 (set)，FastAPI 同样会将其序列化为 JSON 响应。
    # 集合会被序列化成 JSON 数组 (list)。
    # 核心点在于：开发者只关注返回数据，具体的 HTTP 响应封装（如状态码、JSON转换）由 FastAPI 完成。
    return {"hello,world"}


# 这段代码是标准的 Python 启动入口。
# 只有当文件作为主程序运行时（而不是被其他文件导入时），下面的代码块才会执行。
if __name__ == "__main__":
    # 使用 uvicorn.run() 方法启动 ASGI 服务器来运行 FastAPI 应用。
    uvicorn.run("fastapi_test1:app",port=8078,reload=True)
        # 完整的应用指定格式是 "模块名:应用实例名"
        # "fastapi_test1" 假设是你保存这段代码的文件名（例如：fastapi_test1.py）。
        # "app" 是你在文件开头创建的 FastAPI 实例（app = FastAPI()）。

        # port=8078 指定服务器监听的端口号。客户端将通过这个端口访问服务。

        # reload=True 开启热重载（Watchdog）。
        # 当检测到代码文件发生变化时，服务器会自动重启，这极大地提高了开发效率。
        # 注意：在生产环境中通常设置为 False。