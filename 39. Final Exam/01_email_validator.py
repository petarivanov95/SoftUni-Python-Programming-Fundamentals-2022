email = input()

while True:
    command = input().split()
    if command[0] == "Complete":
        break

    if command[0] == "Make":
        if command[1] == "Upper":
            email = email.upper()
        elif command[1] == "Lower":
            email = email.lower()
        print(email)

    elif command[0] == "GetDomain":
        count = int(command[1])
        print(email[-count:])

    elif command[0] == "GetUsername":
        if "@" in email:
            username = email.split("@")[0]
            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")

    elif command[0] == "Replace":
        char = command[1]
        email = email.replace(char, "-")
        print(email)

    elif command[0] == "Encrypt":
        encrypted = " ".join(str(ord(c)) for c in email)
        print(encrypted)

