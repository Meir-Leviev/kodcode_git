import rectangle
import square
import triangle
import hexagon
import circle


r = rectangle.Rectangle(2, 3)
s = square.Square(4)
t = triangle.Triangle(3,4,3,4,5)
h = hexagon.Hexagon(3)
c = circle.Circle(6)
shapes = [r, s, t, h, c]
for shape in shapes:
    print(shape)