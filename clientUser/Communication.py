import socket
from threading import Thread


class Communication:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread = Thread(target=self.receive)
        self.thread.daemon = True
        self.messages = []

    def connect(self):
        self.socket.connect((self.ip, self.port))
        self.socket.send(b'Hello\n')
        self.thread.start()

    def send(self, message):
        self.socket.send(message)

    def receive(self):
        while True:
            result = self.socket.recv(8191)
            if result:
                self.process_message(result)

    def process_message(self, message):
        print(message)
        self.messages.append(message)

    def pop(self):
        return self.messages.pop(0)

    def has_next(self):
        return len(self.messages) > 0
