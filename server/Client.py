from ByteStream import ByteStream
from threading import Thread
from Vector import Vector
import json


class Client:
    def __init__(self, socket, adr):
        self.socket = socket
        self.adr = adr
        self.stream = ByteStream()
        self.thread = Thread(target=self.communicate)
        self.thread.daemon = True
        self.thread.start()
        self.exist = True
        self.commands = []
        self.position = Vector()
        self.send_message = b""


    def communicate(self):
        while True:
            try:
                msg = self.socket.recv(2048)
            except ConnectionResetError:
                print("client at {} closed connection".format(self.adr))
                break

            if msg:
                self.stream.append(msg)
                while self.stream.has_next():
                    self.handle_message(self.stream.read_line())
        self.exist = False

    def handle_message(self, message):
        if message == b'Hello':
            print("client at " + str(self.adr))
        else:
            message = str(message, "ASCII")
            message = json.loads(message)
            self.commands.append(message)

    def send(self, send_message):
        send_message = json.dumps(send_message)
        send_message = bytes(send_message, "ASCII")
        self.send_message += send_message + b"\n"

    def flush(self):
        if self.exist:
            self.socket.send(self.send_message)
            self.send_message = b""

    def has_message(self):
        return len(self.commands) > 0

    def pop(self):
        return self.commands.pop(0)
