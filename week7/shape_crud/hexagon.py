import math
from shape import Shape


class Hexagon(Shape):
    def __init__(self, shape_id, shape_type, side):
        super().__init__(shape_id, shape_type)
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * self.side**2) / 2

    def get_perimeter(self):
        return 6 * self.side

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.shape_type,
            "area": self.get_area()
        }