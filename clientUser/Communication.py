import socket
from threading import Thread
from ByteStream import ByteStream
import json


class Communication:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.thread = Thread(target=self.receive)
        self.thread.daemon = True
        self.messages = []
        self.stream = ByteStream()
        self.send_message = b''

    def connect(self):
        self.socket.connect((self.ip, self.port))
        self.socket.send(b'Hello\n')
        self.thread.start()

    def send(self, message):
        j = json.dumps(message)
        b = bytes(j, "ASCII")
        self.send_message += b + b'\n'

    def flush(self):
        self.socket.send(self.send_message)
        self.send_message = b''

    def receive(self):
        while True:
            msg = self.socket.recv(8191)
            if msg:
                self.stream.append(msg)
                while self.stream.has_next():
                    self.process_message(self.stream.read_line())

    def process_message(self, message):
        s = str(message, 'ASCII')
        d = json.loads(s)
        print(d)
        self.messages.append(d)

    def pop(self):
        return self.messages.pop(0)

    def has_next(self):
        return len(self.messages) > 0
