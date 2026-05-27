from calculator import Shape

class Rectangle(Shape):
    def __init__(self, width,  height):
        self.height = height
        self.width = width
        self.area = width * height
        self.perimeter = 2 * (width + height)
        
