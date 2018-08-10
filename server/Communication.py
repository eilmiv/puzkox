import socketserver
from threading import Thread
import socket


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), "utf-8")
        print(data)

class Communication:
    def __init__(self,port):
        self.myIP = socket.gethostbyname(socket.gethostname())
        self.server = socketserver.ThreadingTCPServer ((self.myIP,port), RequestHandler)

    def start(self):
        thread1 = Thread(target=self.server.serve_forever())
        thread1.daemon=True
        thread1.start()



