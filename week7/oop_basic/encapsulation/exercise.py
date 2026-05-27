# 1
class Student:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name


s = Student('Dana')
print(s.name)

# 2


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

# 3


class Thermometer:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError
        self.celsius = value
        

# 4
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount


# 5
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


# 6
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return (self.value * 9/5) + 32
    

# 7
class Calculator:
    def __init__(self, number):
        pass

    @staticmethod
    def is_even(n):
        return n % 2 == 0
    

# 8
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair: tuple):
        x, y = pair
        return cls(x, y)


# 9
class User:
    users_count = 0
    def __init__(self):

        User.users_count += 1

    @classmethod
    def how_many(cls):
        return cls.users_count
    
# 10
class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError('negative value')
        self._price = new_price