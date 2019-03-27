import socket
import os
from threading import Thread

TARGET_IP = "127.0.0.1"
TARGET_PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((TARGET_IP, TARGET_PORT))

namafile = ["metallica.jpg", "bonjovi.jpg", "a7x.jpg", "OOR.jpg", "moumantai.png"]

def sendImage(TARGET_IP, TARGET_PORT):
    sock.sendto("Mengirim", (TARGET_IP, TARGET_PORT))
    for nama in namafile:
        sock.sendto("awal {}".format(nama), (TARGET_IP, TARGET_PORT))
        ukuran = os.stat(nama).st_size
        fp = open(nama, 'rb')
        k = fp.read()
        terkirim = 0
        for x in k:
            sock.sendto(x, (TARGET_IP, TARGET_PORT))
            terkirim = terkirim + 1
            print "\r terkirim {} of {} ".format(terkirim, ukuran)
        sock.sendto("selesai", (TARGET_IP, TARGET_PORT))
        fp.close()
    sock.sendto("akhir", (TARGET_IP, TARGET_PORT))


while True:
    data, addr = sock.recvfrom(1024)
    print "Request : " + str(addr)
    if (data == "ada"):
        thread = Thread(target=sendImage, args=addr)
        thread.start()
