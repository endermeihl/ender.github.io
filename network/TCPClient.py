import socket

# 创建 TCP/IP 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('localhost', 8888)
sock.connect(server_address)

try:
    # 发送数据给服务器
    message = 'Hello, server!'
    sock.sendall(message.encode())

    # 接收服务器响应数据
    data = sock.recv(1024)
    print('接收到数据:', data.decode())
finally:
    # 关闭连接
    sock.close()