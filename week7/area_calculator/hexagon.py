import math
from calculator import Shape


class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * self.side**2) / 2

    def get_perimeter(self):
        return 6 * self.side
