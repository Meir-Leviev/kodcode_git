# 1
def remove_duplicates(l: list) -> list:
    return list(set(l))


# 2
def count_unique(l: list) -> int:
    s = set(l)
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt


# 3
def common_elements(l1: list, l2: list) -> list:
    s1 = set(l1)
    s2 = set(l2)
    result = list(s1 & s2)
    return sorted(result)


def only_in_one(l1: list, l2: list) -> list:
    s1 = set(l1)
    s2 = set(l2)
    result = list(s1 ^ s2)
    return sorted(result)


# 5
def is_subset(a: list, b: list) -> bool:
    s1 = set(a)
    s2 = set(b)
    return s1 < s2


# 6
def unique_characters(word: str) -> bool:
    word_as_set = set(word)
    return len(word) == len(word_as_set)


# 7
def first_repeated_element(l: list):
    seen = set()
    for item in l:
        if item in seen:
            return item
        else:
            seen.add(item)
    return None


# 8
def distinct_words(sentence: str) -> int:
    as_set = set(sentence.lower().split())
    print(as_set)
    return len(as_set)


# 9
def pair_sum_exists(numbers: list[int], target: int):
    seen = set()
    for n in numbers:
        pair = target - n
        if pair in seen:
            return True
        else:
            seen.add(n)
    return False


# 10
def difference(l1: list, l2: list):
    s1 = set(l1)
    s2 = set(l2)
    check1 = [item for item in s1 if item not in s2]
    check2 = [item for item in s2 if item not in s1]
    result = check1 + check2
    return sorted(result)
