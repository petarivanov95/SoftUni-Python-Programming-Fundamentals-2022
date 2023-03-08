chat = []
while True:
    command_list = input().split(" ")

    if command_list[0] == "end":
        break

    elif command_list[0] == "Chat":
        chat.append(command_list[1])

    elif command_list[0] == "Delete":
        if command_list[1] in chat:
            chat.remove(command_list[1])

    elif command_list[0] == "Edit":
        if command_list[1] in chat:
            special_val = chat.index(command_list[1])
            chat[special_val] = command_list[2]

    elif command_list[0] == "Pin":
        if command_list[1] in chat:
            special_val = chat.index(command_list[1])
            popped = chat.pop(special_val)
            chat.append(popped)

    elif command_list[0] == "Spam":
        for x in range(1, len(command_list)):
            chat.append(command_list[x])


for x in chat:
    print(x)
