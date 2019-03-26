import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("ada", (SERVER_IP, SERVER_PORT))

def getImage():
    while True:
        data, addr = sock.recvfrom(1024)
        if(data[0:5]=="mulai"):
            print data[6:]
            fp = open(data[6:],'wb+')
            ditulis=0
        elif(data=="selesai"):
            fp.close()
        elif(data=="akhir"):
            break
        else:
            print "blok ", len(data), data[0:10]
            fp.write(data)

while True:
    data, addr = sock.recvfrom(1024)
    if(data=="mengirim"):
        print "menerima gambar"
        getImage()