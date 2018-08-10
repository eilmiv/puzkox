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

class CommunicationAlt:
    def __init__(self, port):
        self.port = port
        self.clients = []

        self.accept_thread = Thread(target=self.accept_connections)
        self.accept_thread.daemon = True

    def start(self):
        self.accept_thread.start()

    def update(self):
        for c in self.clients:
            c.update()

    def accept_connections(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', self.port))
        s.listen()
        while True:
            soc, adr = s.accept()
            self.create_client(soc, adr)

    def create_client(self, soc, adr):
        self.clients.append(Client(soc, adr))






