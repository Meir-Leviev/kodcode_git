
# 1
def sum_list(numbers: list[int]) -> int:
    acc = 0
    for n in numbers:
        acc += n
    return acc


# 2
def max_on_list(numbers: list[int]) -> int:
    highest = 0
    for n in numbers:
        if n > highest:
            highest = n
    return highest


# 3
def count_occurrences(lst: list[int], value: int) -> int:
    cnt = 0
    for n in lst:
        if n == value:
            cnt += 1
    return cnt


# 4
def reverse_list(lst: list):
    return list(reversed(lst))
# Did not used reverse() or slicing with [::-1] I used reversed(),
# reversed with a 'd' was not specified.


# 5
def remove_duplicates(lst: list):
    new_lst = []
    for item in lst:
        if item not in new_lst:
            new_lst.append(item)
    return new_lst


#  6

def second_largest(numbers: list[int]) -> int:
    highest = 0
    second = 0
    for n in numbers:
        if n > highest:
            second = highest
            highest = n
        elif n > second and n < highest:
            second = n
    return second


# or
def second_largest2(numbers: list[int]) -> None | int:
    numbers = sorted(numbers)
    numbers = remove_duplicates(numbers)
    if len(numbers) < 1:
        return None
    else:
        return numbers[-2]


# 7
def marge_sort(lst_a: list, lst_b: list):
    new = lst_a.extend(lst_b)
    return sorted(new)


# 8
def rotate_list(lst: list, k: int):
    rotated_list = []
    k = k % len(lst)

    rotated_list.extend(lst[-k:])
    rotated_list.extend(lst[:-k])
    return rotated_list
