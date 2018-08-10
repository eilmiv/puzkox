import socketserver
from threading import Thread
import socket
from server.Client import Client

f=0
Q=0
class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), "utf-8")
        Q.createclient(data)


class Communication:

    def __init__(self,port):
        global f
        global Q
        self.myIP = socket.gethostbyname(socket.gethostname())
        f=self.createclient
        Q=self
        self.server = socketserver.ThreadingTCPServer ((self.myIP,port), RequestHandler)
        self.clients = []

    def start(self):
        thread1 = Thread(target=self.server.serve_forever())
        thread1.daemon=True
        thread1.start()

    def createclient(self,message):
        l=message.split(":")
        if len(l) == 2 and l[0] == 'Hello':
            self.clients.append(Client(l[1]))
            print ("client beigetreten")
        else:
            print ("client send wron data !!!"+message)





