import math
class Vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __repr__(self):
        return "({}, {})".format(self.x,self.y)

    def __add__(self, other):
        return Vector(self.x + other.x,self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return (self.x * other.x + self.y * other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def abs_q(self):
        return self.x ** 2 + self.y **2

    def ang (self, ohter):
        return math.acos(self*ohter/(abs(self)*abs(ohter)))







if __name__ == "__main__":
    Vector1 = Vector(1,0)
    Vector2 = Vector(0.5,0.5)
    print((Vector1.ang(Vector2))/math.pi)