students = {}
while True: 
    command = input()
    if ':' not in command:
        course = command
        break
    else:
        name, id_student, courses = command.split(':')
        students[id_student] = name,courses



for name in students:
    if course in students.get(name):
        print(f'{students.get(name)[0]} - {name}')
