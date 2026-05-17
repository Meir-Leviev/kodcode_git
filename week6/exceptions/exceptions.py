
# 1
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None
    except TypeError:
        return None
    except Exception:
        return None


# 2

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'undefined'


# 3

def read_first_line(path):
    try:
        with open(path, 'r') as f:
            lines = f.readline()
        return lines
    except FileNotFoundError:
        return None


#  4

def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return 'missing'


# 5
def parse_ints(values):
    new_lst = []
    for v in values:
        try:
            v = int(v)
            new_lst.append(v)
        except ValueError:
            continue
    return new_lst


# 6
def set_age(age):
    if 0 > age or age > 150:
        raise ValueError
    else:
        return age


# 7
class InsufficientFundsError(Exception):
    pass


def withdraw(balance: int, amount: int):
    if amount > balance:
        raise InsufficientFundsError
    else:
        return balance - amount


# 8
def retry(func, n):
    last_exception = None
    for attempt in range(n):
        try:
            return func()
        except Exception as e:
            last_exception = e

    if last_exception is not None:
        raise last_exception


def count_errors(funcs: list):
    cnt = 0
    for f in funcs:
        try:
            f()
        except Exception:
            cnt += 1
    return cnt


def load_config(path):
    try:
        with open(path, 'r') as f:
            line = f.readline()
        return int(line)
    except Exception as og_error:
        raise RuntimeError('failed to load config') from og_error
