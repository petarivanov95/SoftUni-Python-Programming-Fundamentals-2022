# Option 1

students = {}

while True:

    command = input()

    if ":" not in command:
        course = command
        break

    else:
        name, id_student, courses = command.split(":")
        students[id_student] = name, courses

for idx in students:
    if course in students.get(idx):
        print(f"{students.get(idx)[0]} - {idx}")


# Option 2
# university = {}
# course = ''
# while True:
#     command = input()
#     if ":" not in command:
#         course = command.replace("_", ' ')
#         break

#     name, number, discipline = command.split(':')
#     if discipline not in university:
#         university[discipline] = []
#     university[discipline].append(f'{name} - {number}')

# print(*university[course], sep='\n')
