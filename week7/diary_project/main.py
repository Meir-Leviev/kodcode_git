import os
# part 1
diary_entries = [
    "2024-01-15: It was a busy day on the project\n",
    "2024-01-16: I learned about File Handling in Python\n",
    "2024-01-17: I completed the first exercise!\n"
]
with open('diary.txt', 'w', encoding='utf-8') as f:
    f.writelines(diary_entries)
print('file created successfully!')

with open('diary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

# part 2


def add_entry(filename, date, content):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f'{date}: {content}')


add_entry('diary.txt', '2024-01-18', 'Wonderful day - finished exercise 1!\n')

# part 3


def search_diary(filename, keyword):
    result = []
    if not safe_read_diary(filename):
        print('file does not exists')
        return
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if keyword in line:
                result.append(line.strip())
    return result


def safe_read_diary(filename):
    return os.path.exists(filename)

