import socket

# 创建 UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地地址和端口
sock.bind(('localhost', 8888))

while True:
    # 接收数据
    data, addr = sock.recvfrom(1024)
    print('Received from {}: {}'.format(addr, data.decode()))

    # 发送数据
    sock.sendto('Hello, World!'.encode(), addr)