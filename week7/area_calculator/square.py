from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)

    def get_perimeter(self):
        return 4 * (self.width)

    def __str__(self):
        return f"Square (Side: {self.width})"