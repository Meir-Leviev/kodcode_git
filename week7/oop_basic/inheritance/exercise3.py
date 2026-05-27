# 1
class Animal:
    def __init__(self):
        pass

    def speak(self):
        return '...'
    
class Dog(Animal):
    def __init__(self):
        pass

    def speak(self):
        return 'WOOF'

# 2
class Vehicle:
    def describe(self):
        return 'A vehicle'
    
class Car(Vehicle):
    pass

print(Car().describe())


# 3
class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

print(Student("Noa", "Kodcode").name)


# 4
class Logger:
    def log(self, msg):
        return msg
    

class TimeLogger(Logger):
    def log(self, msg, time):
        return f'[{time}] ' + super().log(msg)


# 5
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def total_area(shapes):
    """
    Calculates the total area of a mixed list of shapes.
    This is the polymorphic loop.
    """
    total = 0
    for shape in shapes:
        total += shape.area()
    return total


