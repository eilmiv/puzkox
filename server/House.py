from server.Square import Square


class House(Square):
    def __init__(self, position, site_length=1, description="House"):
        super(House, self).__init__(position, site_length, description)