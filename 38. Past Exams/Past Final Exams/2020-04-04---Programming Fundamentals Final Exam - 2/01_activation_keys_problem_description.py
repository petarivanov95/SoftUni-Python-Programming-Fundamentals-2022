activation_key = input()

while True:
    command = input().split(">>>")

    if command[0] == "Generate":
        break

    elif command[0] == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])

        if case == "Upper":
            activation_key = activation_key[:start_index] +\
                             activation_key[start_index:end_index].upper() +\
                             activation_key[end_index:]
        elif case == "Lower":
            activation_key = activation_key[:start_index] +\
                             activation_key[start_index:end_index].lower() +\
                             activation_key[end_index:]

        print(activation_key)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]

        print(activation_key)

print(f"Your activation key is: {activation_key}")
