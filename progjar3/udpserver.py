import socket

SERVER_IP = '10.151.254.132'
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print "diterima", data
    print "dikirim oleh ", addr