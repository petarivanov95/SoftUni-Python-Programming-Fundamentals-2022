command = 0
while command != 'End':
    command = input()
    if command == 'End':
        break
    elif command == "SoftUni":
        continue
    for x in range(len(command)):
        print(command[x]*2,end='')
    print()
