password = input()

while True:
    command = input()
    if command == "Done":
        print(f"Your password is: {password}")
        break

    command_list = command.split()

    if command_list[0] == "TakeOdd":
        password = password[1::2]
        print(password)

    elif command_list[0] == "Cut":
        index, length = int(command_list[1]), int(command_list[2])
        substring = password[index:index + length]
        password = password.replace(substring, "", 1)
        print(password)

    elif command_list[0] == "Substitute":
        substring, substitute = command_list[1], command_list[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
