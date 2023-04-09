message = input()
command = input()

while True:
    commands = command.split(':|:')
    if commands[0] == 'Reveal':
        break
    elif commands[0] == 'InsertSpace':
        idx = int(commands[1])
        message = message[:idx] + " " + message[idx: ]

    elif commands[0] == "Reverse":
        substring = commands[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
        else:
            print("error")
            continue

    elif commands[0] == "ChangeAll":
        substring, replacement = commands[1], commands[2]
        message = message.replace(substring, replacement)

    print(message)
    command = input()

print(f"You have a new text message: {message}")
