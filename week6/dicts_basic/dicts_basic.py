
# 1

def dict_sum(d: dict):
    acc = 0
    for v in d.values():
        acc += v
    return acc


# 2
def max_key_value(d: dict):
    highest = 0
    key = ''
    for k, v in d.items():
        if v > highest:
            highest = v
            key = k
    return key


# 3
def count_chars(your_string: str):
    result = {}
    for char in your_string:
        result[char] = result.get(char, 0) + 1
    return result


# 4
def invert_key_value(d: dict):
    result = {}
    for k, v in d.items():
        result[v] = k
    return result


# 5
def merge_dicts(d1: dict, d2: dict):
    d1.update(d2)
    return d1


# 6
def filter_by_value(d: dict, threshold: int):
    result = {}
    for k, v in d.items():
        if v > threshold:
            result[k] = v
    return result


# 7
def alphabet_order(words: list[str]):
    result = {}
    for word in words:
        result[word[0]] = result.get(word[0], []) + [word]
    return result


# 8
def word_count(words: str):
    words = words.split()
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result


# 9
def common_keys(d1, d2):
    result = []
    for k in d1:
        if k in d2:
            result.append(k)
    return result


# 10
def most_frequent_value(d: dict):
    counter = {}
    for v in d.values():
        counter[v] = counter.get(v, 0) + 1
    return max(counter, key=counter.get)
