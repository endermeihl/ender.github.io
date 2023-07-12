import socket

# 创建 TCP/IP 套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定 IP 地址和端口号
server_address = ('localhost', 8888)
sock.bind(server_address)

# 监听连接请求
sock.listen(1)

while True:
    # 等待客户端连接
    print('等待客户端连接...')
    connection, client_address = sock.accept()
    try:
        print('客户端已连接:', client_address)

        # 接收客户端发送的数据
        data = connection.recv(1024)
        print('接收到数据:', data.decode())

        # 发送响应数据给客户端
        message = 'Hello, client!'
        connection.sendall(message.encode())
    finally:
        # 关闭连接
        connection.close()