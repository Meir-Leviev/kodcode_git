import json

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        self.shapes.append(shape)

    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        for shape in self.shapes:
            if shape['id'] == shape_id:
                shape = new_data
                break

    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape['id'] == shape_id:
                shape.remove(shape)
                break

    def save_to_json(self):
        with open('shapes.json', 'w', encoding='utf-8') as f:
            json.dump(self.shapes, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        with open('shapes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
