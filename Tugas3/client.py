import socket

host = '127.0.0.1'
port = 5000
s = socket.socket()
s.connect((host, port))

def Download():
    filename = raw_input("File Location (folder/filename) -> ")
    if filename != 'q':
        s.send(filename)
        data = s.recv(1024)
        if data[:6] == 'EXISTS':
            filesize = long(data[6:])
            message = raw_input("File exists, " + str(filesize) + "Bytes, download? (Y/N)? -> ")
            if message == 'Y':
                s.send("OK")
                f = open('new_' + filename, 'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while totalRecv < filesize:
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print "{0:.2f}".format((totalRecv / float(filesize)) * 100) + "% Done"

                print "Download Complete!"
                f.close()
        else:
            print "File Does Not Exist!"

def Upload():
    # filename = raw_input("File Location (folder/filename) -> ")
    # if filename != 'q':
    #     s.send(filename)
    #     data = s.recv(1024)
    #     if data[:6] == 'EXISTS':
    #         filesize = long(data[6:])
    #         message = raw_input("File exists, " + str(filesize) + "Bytes, upload? (Y/N)? -> ")
    #         ###??????
    print "Uploading...."

if __name__ == '__main__':
    while True :
        command = raw_input("1. Download \n2. Upload \n Pilih -> " )
        if command == '1':
            Download()
        elif command == '2':
            Upload()
        # else :
        #     s.close()