import math 


# 1
def is_even(n):
    return n % 2 == 0

# 2

def factorial(n: int):
    result = 0
    for i in range(n):
        result *= i
    return result

# 3
def count_vowels(s: str):
    cnt = 0
    for c in s:
        if c.lower() in 'aeiou':
            cnt += 1
    return cnt

# 4
def reversed_string(s: str):
    return s[::-1]

# 5

def find_max(l: list):
    tmp = 0
    for i in l:
        if i > tmp:
            tmp = i

    return tmp

# 6

def celsius_to_fahrenheit(c):
    return ( c * 9 / 5 ) + 32


# 7
def is_palindrome(word):
    flag = True
    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            flag = False
    return flag 

# 8
def even_list(l: list):
    new_lst = []
    for i in l:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst

# 9

def anagram_check(word_a, word_b):
    return sorted(word_a) == sorted(word_b)

# 10

def word_counter(sentence: str):
    my_dict = dict()
    words = sentence.split(' ')
    for w in words:
        my_dict[w] = my_dict.get(w , 0) + 1

    return my_dict

# 11

def calculate_resource_drain(cost, waste_factor):
    """
    Docstring for calculate_resource_drain
    
    :param cost: a number
    :param waste_factor: the percentage number 
                         e.g. 15 is 15% = 0.15
    """
    waste = waste_factor * (10 ** -2)
    return cost * waste

def get_net_recourses(cost, waste_factor):
    return cost - calculate_resource_drain(cost, waste_factor)

# 12

def intercept_length(packet):
    return len(packet)

def verify_transmission(packet):
    return f'Intercepted packet contains {intercept_length(packet)} bytes of data.'

# 13

def convert_to_decibels(signal_strength):
    decibels = 20 * math.log10(signal_strength)
    return decibels

def is_threat_detected(signal_strength):
    db_level = convert_to_decibels(signal_strength)

    if db_level > 90:
        return True
    else:
        return False
    
# 14

def get_fuel_surcharge(distance):
    liters_needed = distance / 10
    fuel_cost = liters_needed * 8
    return fuel_cost * 0.17

def get_hazard_pay(distance):
    liters_needed = distance / 10
    fuel_cost = liters_needed * 8
    return fuel_cost * 0.05

def calculate_mission_cost(distance):
    base_cost = (distance / 10) * 8
    surcharge = get_fuel_surcharge(distance)
    hazard = get_hazard_pay(distance)

    total_budget = base_cost + surcharge + hazard
    return total_budget
    