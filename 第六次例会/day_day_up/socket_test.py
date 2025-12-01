import socket

sock=socket.socket()#初始化并创建一个基于 TCP/IP 协议的套接字对象，作为后续步骤中服务器程序对外提供服务的主监听端口

sock.bind(("127.0.0.1",7050)) #绑定本机端口  也就是设定服务器地址和端口，之后通过访问
sock.listen(5)  #最大监听数
while 1:
    # conn  连接服务器的客户端的套接字  conn是客户端与服务端通信的管道,可收可发 conn.receive()  conn.send()
    # addr 客户端的远程地址
    conn, addr=sock.accept()  #阻塞等待客户端连接
    data=conn.recv(1024)           #接收1K的数据
    print("客户端发送的请求信息: ",data) #data就是前面说过的请求格式
    #响应格式:响应首行 响应头 响应体
    conn.send(b"HTTP/1.1 200 OK \r\nusername: cai \r\n\r\n hello world ")  #网络传输的底层本质是二进制数据
    # conn.send(b"HTTP/1.1 200 OK \r\nusername: cai content-type:text/html\r\n\r\n <h1>hello world <h1>")
    conn.close()        #管道关闭,一次通信结束



