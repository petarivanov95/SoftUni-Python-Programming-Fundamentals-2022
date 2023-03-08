wagons = int(input())
my_train = [0 for x in range(wagons)]

command = ""
while command != "End":
    command = input()
    command_list = command.split()
    if "add" in command_list:
        my_train[-1] += int(command_list[-1])

    elif "insert" in command_list:
        my_train[(int(command_list[1]))] += int(command_list[2])

    elif "leave" in command_list:
        my_train[(int(command_list[1]))] -= int(command_list[2])

print(my_train)
