#!../venv/bin/python

import socket

# 创建一个socket对象
server = socket.socket()


# 地址 是一个元祖
addr = ('127.0.0.1',8080)

# 绑定地址
server.bind(addr)

# 监听
server.listen(10)

# 开启服务
print('服务开启，等待连接')
client_socket,client_addr = server.accept()
while True:
    # 接受客户端信息
    recv_msg = client_socket.recv(1024)
    print(recv_msg)
    # 发送消息
    send_msg = input('请输入要发送的消息:')
    client_socket.send(send_msg.encode('utf-8'))