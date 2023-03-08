courses = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student_name = command.split(" : ")
    if course_name in courses:
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]


for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student_name in students:
        print(f"-- {student_name}")
