budget = int(input())
command = input()

while command != "End":
    budget -= int(command)
    if budget < 0:
        print("You went in overdraft!")
        break
    else:
        command = input()

if command == "End" and budget >= 0:
    print("You bought everything needed.")
