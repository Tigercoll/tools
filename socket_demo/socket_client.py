#!../venv/bin/python

import socket

client = socket.socket()

# 地址 是一个元祖
addr = ('127.0.0.1',8080)
# 连接服务器
client.connect(addr)

while True:
    # 发送消息
    send_msg = input('请输入要发送的消息:')
    client.send(send_msg.encode('utf-8'))
    # 接受消息
    recv_msg = client.recv(1024)
    print(recv_msg)