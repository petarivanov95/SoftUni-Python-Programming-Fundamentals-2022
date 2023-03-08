rows = int(input())
students = {}


def average(lst):
    return sum(lst) / len(lst)


for info in range(rows):
    student = input()
    grade = float(input())
    if student in students:
        students[student].append(grade)
    else:
        students[student] = [grade]

final_directory = {x: average(y) for x, y in students.items() if average(y) >= 4.50}

for name, averageGrade in final_directory.items():
    print(f"{name} -> {averageGrade:.2f}")
