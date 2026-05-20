import math

# 1
count = 0


def bump() -> None:
    global count
    count += 1


def value() -> int:
    return count


bump()
bump()
bump()
print(value())


# 2
def make_counter():
    cnt = 0

    def step():
        nonlocal cnt
        cnt += 1
        return cnt

    return step


c = make_counter()
c()
c()
c()
print(c())


# 3
x = "global"
# This code will print 'local' 'enclosing' 'global'


def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()
    print(x)


outer()
print(x)


# 4
# list = [1, 2, 3]
# print(list(range(5)))
# This doesn't work because you used the name list
list_a = [1, 2, 3]
print(list(range(5)))


# 5 in mathutils.py and main.py

# 6 in tools.py

# 7
# import datetime as dt; print(dt.datetime.now())


# 8
def public_names(module):
    lst = dir(module)
    result = []
    for item in lst:
        if not item.startswith("_"):
            result.append(item)
    return result


s = public_names(math)
print(s)
