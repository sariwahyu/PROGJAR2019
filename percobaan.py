import sys
import socket

#create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port
server_address = ('localhost', 10000)
print >> sys.stderr, 'starting app on %s port %s' %server_address
sock.bind(server_address)

#listen for incoming connection
sock.listen(1)
while True:
    print >> sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    print sys.stderr, 'connection from ', client_address

#recieve the data in small chunk and retransmit it
    while True:
        data = connection.recv(32)
        print >> sys.stderr, 'recieve %s' %data
        if data:
            print >> sys.stderr, 'sending data back to the client'
            connection.sendall('-->'+data)
        else:
            print >> sys.stderr, 'no more data from', client_address
            break
            #cleam up the connection
            connection.close()