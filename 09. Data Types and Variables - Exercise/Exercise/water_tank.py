tank_capacity = 255
my_lines = int(input())
tank_current = 0

for x in range(my_lines):
    new_quantity = int(input())
    if new_quantity + tank_current > tank_capacity:
        print("Insufficient capacity!")
    else:
        tank_current += new_quantity

print(tank_current)
