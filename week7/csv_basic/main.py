
def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),
    ]
    with open(filename, 'w', encoding='utf-8') as f:
        for name, grades in students:
            grades = [str(grade) for grade in grades]
            csv_grade = ','.join(grades)
            f.write(f'{name},{csv_grade}\n')


create_grades_file('grades.txt')


def calculate_averages(filename):
    averages = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split(',')
            name = line[0]
            grades = line[1:]
            grades = [int(g) for g in grades]
            avg = round(sum(grades) / len(grades), 2)
            averages[name] = avg
    return averages


results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')


def save_results(averages: dict, output_filename):
    averages = dict(sorted(averages.items(), key=lambda item: item[1]))
    avgs = list(averages.values())
    total_students = len(avgs)
    class_avg = sum(avgs) / total_students
    sorted_items = list(averages.items())
    lowest_student, lowest_avg = sorted_items[0]
    highest_student, highest_avg = sorted_items[-1]
    passing_count = sum(1 for avg in avgs if avg >= 60)
    output_lines = [
        "=== Statistics ===",
        f"Class average: {class_avg:.1f}",
        f"Highest: {highest_student} ({highest_avg:.1f})",
        f"Lowest: {lowest_student} ({lowest_avg:.1f})",
        f"Passing (>=60): {passing_count}/{total_students}\n"
    ]
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('=== Student Results ===\n')
        cnt = 1
        for name, avg in averages.items():
            f.write(f'{cnt}. {name}: {avg:.1f}\n')
            cnt += 1
        for line in output_lines:
            f.write(line + '\n')


averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')
