import shape_manager as sm
import circle
import hexagon
import rectangle
import square
import triangle


def print_main_menu():
    print("\n--- Main Menu ---")
    print("1. Add shape")
    print("2. Show all shapes")
    print("3. Update shape")
    print("4. Delete shape")
    print("5. Exit")


def print_shapes_menu():
    print("\n-- Choose shape to add --")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Triangle")
    print("5. Hexagon")


def create_id(manager):
    shapes = manager.get_all_shapes()
    if shapes:
        last_id = int(shapes[-1].get("id"))
        return last_id + 1
    return 1


def set_square(shape_id):
    side = float(input("Enter square side length: "))
    shape = square.Square(shape_id, "Square", side)
    return shape


def set_rectangle(shape_id):
    width = float(input("Enter rectangle width: "))
    height = float(input("Enter rectangle height: "))
    shape = rectangle.Rectangle(shape_id, "Rectangle", width, height)
    return shape


def set_circle(shape_id):
    radius = float(input("Enter circle radius: "))
    shape = circle.Circle(shape_id, "Circle", radius)
    return shape


def set_triangle(shape_id):
    width = float(input("Enter triangle width (base): "))
    height = float(input("Enter triangle height: "))
    side_a = float(input("Enter side A length: "))
    side_b = float(input("Enter side B length: "))
    side_c = float(input("Enter side C length: "))
    shape = triangle.Triangle(
        shape_id, "Triangle", width, height, side_a, side_b, side_c
    )
    return shape


def set_hexagon(shape_id):
    side = float(input("Enter hexagon side length: "))
    shape = hexagon.Hexagon(shape_id, "Hexagon", side)
    return shape


def main():
    manager = sm.ShapeManager()

    while True:
        print_main_menu()
        main_choice = input(">>> ")

        if main_choice == "1":
            print_shapes_menu()
            shape_choice = input(">>> ")

            shape_id = create_id()
            print(f"New shape ID = {shape_id}")

            shape = None
            try:
                if shape_choice == "1":
                    shape = set_square(shape_id)

                elif shape_choice == "2":
                    shape = set_rectangle(shape_id)

                elif shape_choice == "3":
                    shape = set_circle(shape_id)

                elif shape_choice == "4":
                    shape = set_triangle(shape_id)

                elif shape_choice == "5":
                    shape = set_hexagon(shape_id)

                else:
                    print("Invalid shape choice.")
                    continue

                if shape:
                    data = shape.to_dict()
                    manager.create_shape(data)
                    manager.save_to_json()
                    print(f"{shape.shape_type} added successfully.")

            except ValueError as e:
                print(f"{e}. try again")

        elif main_choice == "2":
            print("-- All Shapes --")
            shapes = manager.get_all_shapes()
            if not shapes:
                print("No shapes found in memory. ")
            else:
                for shape in shapes:
                    print(shape)

        elif main_choice == "3":
            try:
                shape_id = int(input("Enter shape ID to update: "))
                shapes = manager.get_all_shapes()
                old_shape = None
                for shape in shapes:
                    if shape.get("id") == shape_id:
                        old_shape = shape
                        print("Shape found")
                        break
                if old_shape is None:
                    print("Shape not found")
                    continue

                shape_type = old_shape.get("type").lower()
                print(f"Detected shape type: {old_shape.get('type')}")

                if shape_type == "square":
                    shape = set_square(shape_id)

                elif shape_type == "rectangle":
                    shape = set_rectangle(shape_id)

                elif shape_type == "circle":
                    shape = set_circle(shape_id)

                elif shape_type == "triangle":
                    shape = set_triangle(shape_id)

                elif shape_type == "hexagon":
                    shape = set_hexagon(shape_id)

                # save the update
                if shape:
                    new_data = shape.to_dict()
                    manager.update_shape(shape_id, new_data)
                    manager.save_to_json()
                    print(f"Shape ID {shape_id} updated successfully.")

            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif main_choice == "4":
            try:
                shape_id = int(input("Enter shape ID to delete: "))
                manager.delete_shape(shape_id)
                manager.save_to_json()
                print(f"Shape ID {shape_id} deleted.")
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif main_choice == "5":
            print("Saving data and exiting...")
            manager.save_to_json()
            break

        else:
            print("Invalid choice, please try again .")


if __name__ == "__main__":
    main()
