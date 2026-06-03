from shape import Shape

class Rectangle(Shape):
    def __init__(self, shape_id, shape_type, width, height):
        super().__init__(shape_id, shape_type)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.shape_type,
            "area": self.get_area()
        }
