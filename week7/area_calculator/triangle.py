from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height, side_a, side_b, side_c):
        super().__init__(width=base, height=height)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    def get_area(self):
        return super().get_area() / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
