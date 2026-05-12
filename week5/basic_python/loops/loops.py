#  1.

for i in range(1, 10):
    if i % 2 == 0:
        continue
    elif i == 7:
        break
    print(i)
# it prints 1 , 3 , 5

# 2 .

while True:
    u_password = input('Please enter the password: ')

    if u_password == '1234':
        print('Welcome!')
        break
    else:
        print('Try again.')

# 3.

products = []

while True:
    item = input('Please enter an item: ')
    if item == 'done':
        break
    else:
        products.append(item)
print(products)

# while true is the right choice because we do not know when to stop

# 3.2

for row in range(1,4):
    for col in range(1,4):
        if col == 2:
            break
        print(row , col)

# 4.

u_str = input('please enter a string: ')

vowel_cnt = 0
for i in u_str:
    if i.lower() in 'aeiou':
        vowel_cnt += 1
print(vowel_cnt)

# 5.


for i in range(1,6):
    for j in range(1,6):
        print(f'{i} x {j} = {i*j}')

# 6. 

word = input('please enter a word: ')

reversed = ''

for i in range(len(word)):
    reversed += word[-i-1]
print(reversed)

# 7.

num = int(input('please enter a three digit number: '))
temp_n = num
count = 0

while temp_n > 0:
    digit = temp_n % 10
    
    if digit % 2 == 0:
        count = count + 1
        
    temp_n = temp_n // 10

print("Total even digits:", count)

# 8.

text = input('please enter a string: ')
doubled_text = ""


for char in text:
    doubled_text = doubled_text + (char * 2)

print(doubled_text)

# 9.

highest_num = 0

while True:
    num = int(input('please enter a number: '))
    if num == 0:
        break
    elif num > highest_num:
        highest_num = num
print(f'The highest num in {highest_num}')
    
# 10.

my_str = input('please enter a string: ')

only_char_or_nums = True

for c in my_str:
    if not c.isalnum():
        only_char_or_nums = False
        break
print(only_char_or_nums)

# 11.

my_int = int(input('please enter an integer: '))
reversed_num = 0

while my_int > 0:
    digit = my_int % 10
    
    reversed_num = (reversed_num * 10) + digit

    my_int = my_int // 10

print(reversed_num)
