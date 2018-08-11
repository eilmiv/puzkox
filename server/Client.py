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
        self.position = Vector(7,8)
        self.send_message = b""
        self.size = Vector()


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

    def handle_event (self, request, **message):
        if request == "size":
            self.size = Vector (message["width"], message["height"])
            print(self.size)
        if request == "key_down":
             print(message['value'])
        if request == "ping":
            self.send("root", "ping-answer", True, time=message["time"])


    def send(self, target, request, auto_flush=False, **kwargs):
        kwargs ["target"] = target
        kwargs ["request"] = request
        kwargs = json.dumps(kwargs)
        kwargs = bytes(kwargs, "ASCII")
        self.send_message += kwargs + b"\n"
        if auto_flush:
            self.flush()

    def flush(self):
        if self.exist and self.send_message != b"":
            try:
                self.socket.send(self.send_message)
            except ConnectionResetError:
                print("client at {} closed connection".format(self.adr))
                self.exist = False
            self.send_message = b""

    def has_message(self):
        return len(self.commands) > 0

    def pop(self):
        return self.commands.pop(0)

    def send_coordinates(self):
        self.send("view_window", "update", key="location", x=self.position.x, y=self.position.y)



