from Vector import Vector
from server.GameObject import GameObject
from server.Player import Player
from server.Meadow import Meadow
from server.House import House
from server.Bullet import Bullet
from server.ChargedBullet import ChargedBullet
import math


class TestGameObject(GameObject):
    def __init__(self, v):
        super(TestGameObject, self).__init__(Vector())
        self.v = v

    def vertices(self):
        return self.v


if __name__ == "__main__":
    print("Starting Test")
    sq1 = TestGameObject([Vector(x, y) for x, y in ((1,1), (-1,1), (-1,-1), (1,-1))])
    sq2 = TestGameObject([Vector(x, y) for x, y in ((0,0), (2, 0), (2,  2), (0, 2))])
    sq3 = TestGameObject([Vector(x, y) for x, y in ((100, 100), (101, 100), (101, 101), (100, 101))])
    ln1 = TestGameObject([Vector(x, y) for x, y in ((-2, 10), (10, -2))])
    ln2 = TestGameObject([Vector(x, y) for x, y in ((10, 10), (-10, -10))])
    ta1 = TestGameObject([Vector(x, y) for x, y in ((3, -1), (2, -4), (4, -4))])
    ta2 = TestGameObject([Vector(x, y) for x, y in ((1, -2), (5, -3), (5, -1))])
    print("sq1 / sq2:", sq1.colliding(sq2), sq2.colliding(sq1))
    print("sq1 / sq3:", sq1.colliding(sq3), sq3.colliding(sq1))
    print("sq2 / sq3:", sq2.colliding(sq3), sq3.colliding(sq2))
    print("sq1 / ln1:", sq1.colliding(ln1), ln1.colliding(sq1))
    print("ln1 / ln2:", ln1.colliding(ln2), ln2.colliding(ln1))
    print("ln1 / ln1:", ln1.colliding(ln1), ln1.colliding(ln1))
    print("ta1 / ta2:", ta1.colliding(ta2), ta2.colliding(ta1))
    print()

    pl1 = Player(Vector(), 0, Vector(2, 4))
    pl2 = Player(Vector(-1, 0.5), math.pi * 3 / 8, Vector(2, 4))
    pl3 = Player(Vector(500, 0), -0.5 * math.pi, Vector(2, 4))
    print("pl1 / pl2:", pl1.colliding(pl2), pl2.colliding(pl1))
    print("pl1 / pl3:", pl1.colliding(pl3), pl3.colliding(pl1))
    print("pl2 / pl3:", pl2.colliding(pl3), pl3.colliding(pl2))
    print()

    me1 = Meadow(Vector())
    me2 = Meadow(Vector(1,0))
    me3 = Meadow(Vector(1,1), 2)
    ho1 = House(Vector(0,1))
    ho2 = House(Vector(500,500))
    ho3 = House(Vector(0.5, 0.5))
    print("me1 / me1:", me1.colliding(me1))
    print("me1 / me2:", me1.colliding(me2), me2.colliding(me1))
    print("me1 / ho1:", me1.colliding(ho1), ho1.colliding(me1))
    print("me2 / ho1:", me2.colliding(ho1), ho1.colliding(me2))
    print("me1 / ho2:", me1.colliding(ho2), ho2.colliding(me1))
    print("me1 / pl1:", me1.colliding(pl1), pl1.colliding(me1))
    print("me1 / ho3:", me1.colliding(ho3))
    print("me1 / me3:", me1.colliding(me3))
    print()

    bu1 = Bullet(Vector(), 0.1)
    bu2 = Bullet(Vector(0, 1), 0.1)
    cb1 = ChargedBullet(Vector(2, 2), 1)
    cb2 = ChargedBullet(Vector(0, 2), 1)
    print("bu1 / me1:", bu1.colliding(me1))
    print("cb1 / me1:", cb1.colliding(me1))
    print("cb2 / bu2:", cb2.colliding(bu2))
    print("me1 / cb2:", me1.colliding(cb2))
