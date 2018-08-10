import socket

class Communication:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.myIP = socket.gethostbyname(socket.gethostname())
        self.messages = []

    def connect(self):
        self.socket.connect((self.ip, self.port))
        self.socket.setblocking(False)
        self.socket.send(bytes("Hello:{}".format(self.myIP), 'utf-8'))

    def send(self, message):
        self.socket.send(message)

    def update(self):
        result = self.socket.recv(8191)
        if result:
            self.process_message(result)

    def process_message(self, message):
        self.messages.append(message)

    def pop(self):
        return self.messages.pop(0)
