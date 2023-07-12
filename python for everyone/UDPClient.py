import socket

# 创建 UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据
sock.sendto('Hello, Server!'.encode(), ('localhost', 8888))

# 接收数据
data, addr = sock.recvfrom(1024)
print('Received from {}: {}'.format(addr, data.decode()))

# 关闭 Socket
sock.close()