from server.Bullet import Bullet


class ChargedBullet(Bullet):
    def __init__(self, position, radius, description="charged bullet"):
        super(ChargedBullet, self).__init__(position, radius, description)

    def serialize(self):
        pass