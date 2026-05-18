
# 1
def sum_tuple(t: tuple[int]) -> int:
    acc = 0
    for n in t:
        acc += n
    return acc


# 2
def max_tuple(t: tuple[int]) -> int:
    if t:
        return sorted(t)[-1]


# 3
def count_occurrences(t: tuple[int], value):
    cnt = 0
    for n in t:
        if n == value:
            cnt += 1
    return cnt


# 4
def reverse_tuple(t: tuple) -> tuple:
    return tuple(reversed(t))


# 5
def swap_pairs(t: tuple):
    if len(t) % 2 == 0:
        result = ()
        for i in range(0, len(t), 2):
            result += t[i + 1], t[i]
        return result


# 6
def min_max(t: tuple):
    if t:
        sorted_t = sorted(t)
        return sorted_t[0], sorted_t[-1]


# 7
def distance_between_points(t1: tuple, t2: tuple):
    x1, y1 = t1
    x2, y2 = t2
    dis_x = x2 - x1
    dis_y = y2 - y1
    distance = (dis_x**2 + dis_y**2) ** 0.5
    return distance


# 8
def merge_and_sort(t1, t2):
    new_t = t1 + t2
    sorted_t = tuple(sorted(new_t))
    return sorted_t


# 9
def frequency_table(t: tuple):
    result = ()
    for item in t:

        cnt = item, count_occurrences(t, item)
        if cnt not in result:
            result += (cnt,)

    return result


# 10
def rotate_tuple(t: tuple, k):
    result = ()
    k = k % len(t)
    result += t[-k:]
    result += t[:-k]
    return result
