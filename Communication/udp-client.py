import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 5001
client.bind(('', port))

client.sendto(b"12345",("127.0.0.1", 5000))
