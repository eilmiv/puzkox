from server.Player import Player
class Client:
    def __init__(self,ip):
        self.ip=ip
        self.player=Player()