import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 5000
server.bind(('', port))

data, addr = server.recvfrom(4096)

print(data)
