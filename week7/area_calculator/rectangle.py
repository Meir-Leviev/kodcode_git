from calculator import Shape

class Rectangle(Shape):
    def __init__(self, width,  height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle (Width: {self.width}, Height: {self.height})"
