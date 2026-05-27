from shape import Shape

class Triangle(Shape):
    def __init__(self, shape_id, shape_type,
                 width, height, side_a, side_b, side_c):
        super().__init__(shape_id, shape_type)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.height = height
        self.width = width
        
    def get_area(self):
        return (self.height * self.width) / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
    
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.shape_type,
            "area": self.get_area()
        }
