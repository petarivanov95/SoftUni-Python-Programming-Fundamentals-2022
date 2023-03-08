command = 1
reg_percent = 0.2
spec_percent = 0.1
total = 0
taxes = 0
while True:
    command = input()
    if command == "special":
        break
    if command == "regular":
        break
    if float(command) > 0:
        total += float(command)
    elif float(command) < 0:
        print("Invalid price!")
    elif float(command) == 0:
        print("Invalid order!")

if command == "regular":
    if total == 0:
        print("Invalid order!")
    else:
        taxes = reg_percent * total
        final_result = taxes + total
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {final_result:.2f}$")
elif command == "special":
    if total == 0:
        print("Invalid order!")
    else:
        taxes = reg_percent * total
        final_result = (1 - spec_percent) * (taxes + total)

        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {final_result:.2f}$")
