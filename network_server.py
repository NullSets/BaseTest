


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)

while True:
    sock,addr = s.accept()
    print("Got connection from %s:%s" % addr)
    sock.send("Thank you for connecting".encode("utf-8"))
    sock.close()

