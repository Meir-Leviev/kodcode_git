import circle
import hexagon
import rectangle
import square
import triangle


def check_if_numeric(user_input):
    """Function that checks if the input is a valid number"""
    try:
        float(user_input)
        return True
    except ValueError:
        print("Error: Input must be a valid number")
        return False


def check_if_positive(number):
    """Function that checks if the number is greater than zero"""
    if number <= 0:
        print("Side must be greater than 0")
        return False
    return True


def get_input(prompt):
    """Function that gets the input and uses the two validations above"""
    while True:
        user_input = input(prompt)
        
        # First check: Is it a number?
        if check_if_numeric(user_input) == False:
            continue
            
        # Second check: Is it positive?
        number = float(user_input)
        if check_if_positive(number) == False:
            continue
            
        return number

if __name__ == "__main__":
    # Rectangle
    rect_width = get_input("Enter width: ")
    rect_height = get_input("Enter height: ")
    r = rectangle.Rectangle(rect_width, rect_height)
    
    # Square
    sq_side = get_input("Enter side length: ")
    s = square.Square(sq_side)
    
    # Triangle
    t_side1 = get_input("Enter side 1: ")
    t_side2 = get_input("Enter side 2: ")
    t_side3 = get_input("Enter side 3: ")
    t_base = get_input("Enter base: ")
    t_height = get_input("Enter height: ")
    t = triangle.Triangle(t_side1, t_side2, t_side3, t_base, t_height)
    
    # Hexagon
    hex_side = get_input("Enter side length: ")
    h = hexagon.Hexagon(hex_side)
    
    # Circle
    radius = get_input("Enter radius: ")
    c = circle.Circle(radius)
    
    # Print results
    shapes = [r, s, t, h, c]
    for shape in shapes:
        print(shape)