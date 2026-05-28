import json
import os

class ShapeManager:
    def __init__(self):
        self.shapes = []
        self.load_from_json()

    def create_shape(self, shape):
        self.shapes.append(shape)

    def get_all_shapes(self):
        return self.shapes

    def update_shape(self, shape_id, new_data):
        for i, shape in enumerate(self.shapes):
            if shape.get('id') == shape_id:
                self.shapes[i] = new_data
                break

    def delete_shape(self, shape_id):
        for shape in self.shapes:
            if shape.get('id') == shape_id:
                self.shapes.remove(shape)
                break

    def save_to_json(self):
        with open('shapes.json', 'w', encoding='utf-8') as f:
            json.dump(self.shapes, f, indent=4)

    def load_from_json(self):
        # Check if the file exists before trying to open it
        if os.path.exists('shapes.json'):
            try:
                with open('shapes.json', 'r', encoding='utf-8') as f:
                    self.shapes = json.load(f)
            except json.JSONDecodeError:
                # Handle empty or corrupted JSON file
                self.shapes = []
        else:
            self.shapes = []
