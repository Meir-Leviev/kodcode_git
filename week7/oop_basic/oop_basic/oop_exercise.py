

# 1
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f'{self.name} says woof'


# 2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 3
class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.count += 1

    def value(self):
        return self.value


# 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


# 5
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= amount


# 6
class Temperature:
    def __init__(self, value_in_c):
        self.value = value_in_c

    def to_fahrenheit(self):
        return (self.value * 9/5) + 32


# 7
class Student:
    school = 'KodCode'

    def __init__(self,  name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


student1 = Student('Asher')
student2 = Student('Ronen')
print(student1.name)
student2.chang_name('Eyal')
print(student1.name)


# 8
class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1


# 9
class Money:
    def __init__(self, amount):
        self.amount = amount

    def is_more_than(self, other):
        return self.amount > other.amount


# 10
class PlayList:
    def __init__(self, song_titles):
        self.songs = song_titles

    def add(self, title):
        self.songs.append(title)

    def remove(self, title):
        self.songs.remove(title)

    def count(self):
        return len(self.songs)

    def __str__(self):
        playlist_str = ''
        for song in self.songs:
            playlist_str += f'{song}.\n'
        return playlist_str
