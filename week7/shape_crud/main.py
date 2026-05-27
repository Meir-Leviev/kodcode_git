import shape_manager as sm
import circle
import hexagon
import rectangle
import square
import triangle

if __name__ == "__main__":
    # Create ONE instance of the manager to use throughout the program
    manager = sm.ShapeManager()

    print('-- Choose shape --')
    print('1. Square')
    print('2. Rectangle')
    print('3. Circle')
    choice = input('>>> ')

    shape = None

    if choice == '1':
        shape = square.Square(1, 'square', 4)
    elif choice == '2':
        shape = rectangle.Rectangle(2, 'rectangle', 3, 4)
    elif choice == '3':
        shape = circle.Circle(3, 'Circle', 4.5)
    else:
        print("Invalid choice!")

    # Only proceed if a valid shape was created
    if shape:
        data = shape.to_dict()
        manager.create_shape(data)
        
        print("\nCurrent shapes in memory:")
        print(manager.get_all_shapes())
        
        # Save changes to the file
        manager.save_to_json()