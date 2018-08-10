from server.Player import Player
from ByteStream import ByteStream
from threading import Thread


class Client:
    def __init__(self, socket, adr):
        self.socket = socket
        self.adr = adr
        self.player = Player()
        self.stream = ByteStream()
        self.thread = Thread(target=self.communicate)
        self.thread.daemon = True
        self.thread.start()
        self.exist = True

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

    def update(self):
        self.player.update()
        self.send(b"lol")

    def handle_message(self, message):
        if message == b'Hello':
            print("client at " + str(self.adr))
        print(message)

    def send(self, message):
        if self.exist:
            self.socket.send(message)
