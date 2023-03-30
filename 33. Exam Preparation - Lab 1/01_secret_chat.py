# Read the original message from standard input
message = input()

# Keep reading commands until the "Reveal" command is received
while True:
    command = input()
    if command == "Reveal":
        # If the "Reveal" command is received, break out of the loop
        break

    # Split the command into the action and its parameters
    action, *params = command.split(":|:")

    if action == "InsertSpace":
        # If the action is "InsertSpace", get the index to insert the space
        index = int(params[0])
        # Insert the space at the specified index
        message = message[:index] + " " + message[index:]

    elif action == "Reverse":
        # If the action is "Reverse", get the substring to reverse
        substring = params[0]
        if substring in message:
            # If the substring is in the message, reverse it and replace the original substring with the reversed one
            reversed_substring = substring[::-1]
            message = message.replace(substring, "", 1) + reversed_substring
        else:
            # If the substring is not in the message, print an error message and continue with the next command
            print("error")
            continue

    elif action == "ChangeAll":
        # If the action is "ChangeAll", get the substring and replacement text
        substring, replacement = params
        # Replace all occurrences of the substring with the replacement text
        message = message.replace(substring, replacement)

    # Print the current state of the message after the action is performed
    print(message)

# Print the final state of the message after all commands are performed
print(f"You have a new text message: {message}")
