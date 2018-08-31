from server.Square import Square


class Street(Square):
    def __init__(self, position, site_length=1, description="Street"):
        super(Street, self).__init__(position, site_length, description)

    def serialize(self):
        return {"location_x":self.position.x, "location_y":self.position.y, "texture":"street"}