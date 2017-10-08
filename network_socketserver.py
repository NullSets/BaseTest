
# from socketserver import TCPServer,StreamRequestHandler
#
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.client_address
#         print("Got connection from",addr)
#         self.wfile.write(("Thank you for connecting").encode("utf-8"))
#
# server = TCPServer(("",1234),Handler)
# server.serve_forever()


# 使用交叉 (windows 不支持交叉)
# from socketserver import TCPServer,ForkingMixIn,StreamRequestHandler
#
# class Server(ForkingMixIn,TCPServer):
#     pass
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.client_address
#         print("Got connection from",addr)
#self.wfile.write(("Thank you for connecting").encode("utf-8"))
# server = Server(("",1234),Handler)
# server.serve_forever()


# 使用线程处理
# from socketserver import TCPServer,ThreadingMixIn,StreamRequestHandler
#
# class Server(ThreadingMixIn,TCPServer):
#     pass
# class Handler(StreamRequestHandler):
#     def handle(self):
#         addr = self.client_address
#         print("Got connection from",addr)
#         self.wfile.write(("Thank you for connecting").encode("utf-8"))
# server = Server(("",1234),Handler)
# server.serve_forever()


# 带有select 和 poll（UNIX中使用） 的异步I/O
import socket,select
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(5)
inputs = [s]
while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr = s.accept()
            print("Got connection from",addr)
            inputs.append(c)
    else:
        try:
            data = r.recv(1024)
            disconnected = not data
        except socket.error:
            disconnected = True

        if disconnected:
            print(r.client_address,'disconnected')
            inputs.remove(r)
        else:
            print(data)





