phonebook = {}

while True:
    my_input = input()
    if "-" not in my_input:
        break
    person, phone = my_input.split("-")
    phonebook[person] = phone

for x in range(int(my_input)):
    check = input()
    if check in phonebook.keys():
        print(f"{check} -> {phonebook[check]}")
    else:
        print(f"Contact {check} does not exist.")
