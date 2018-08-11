from threading import Thread
import socket
from server.Client import Client


class Communication:
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






