from ByteStream import ByteStream
from threading import Thread
from Vector import Vector
import json
import math
import server.options as options

class Client:
    def __init__(self, socket, adr):
        self.area = 20
        self.socket = socket
        self.adr = adr
        self.stream = ByteStream()
        self.exist = True
        self.commands = []
        self.position = Vector(0,0)
        self.send_message = b""
        self.size = Vector()
        self.relative_size = Vector(1, 1)
        self.send("image_provider", "sizes", block_x=1, block_y=1, car_x=options.player_size.x, car_y=options.player_size.y)
        self.player = None

        self.thread = Thread(target=self.communicate)
        self.thread.daemon = True
        self.thread.start()


    def communicate(self):
        while True:
            try:
                msg = self.socket.recv(2048)
            except ConnectionResetError:
                print("client at {} closed connection - communicate".format(self.adr))
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
            a = message["width"] / message["height"]

            y = math.sqrt(self.area / a)
            x = a*y
            #print("y=",y)
            #print("x=",x)
            #print((x / y)/a)
            self.send("view_window", "update", key="size", x=x, y=y)
            self.send("root", "size", x=x, y=y)
            self.relative_size = Vector(x, y)
        if request == "key":
            if self.player:
                v=message["value"]
                if v == "forward":
                    self.player.forward = message['is_down']
                if v == "backward":
                    self.player.backward = message['is_down']
                if v == "left":
                    self.player.left = message['is_down']
                if v == "right":
                    self.player.right = message["is_down"]

                if v == "bullet":
                    if message ["is_down"]:
                        self.player.shoot()

            #print(message['value'])
        if request == "ping":
            self.send("root", "ping-answer", True, time=message["time"])



    def send(self, target, request, auto_flush=False, **kwargs):
        kwargs["target"] = target
        kwargs["request"] = request
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
                print("client at {} closed connection - flush".format(self.adr))
                self.exist = False
            self.send_message = b""

    def has_message(self):
        return len(self.commands) > 0

    def pop(self):
        return self.commands.pop(0)

    def send_coordinates(self):
        self.send("view_window", "update", key="location", x=self.position.x, y=self.position.y)

    def update(self, colliding, delta):
        if self.player:
            self.position = self.player.position-self.relative_size/2

        for obj in colliding:
            if obj.exist:
                self.send("scene", "create", id=obj.id, **obj.serialize())





