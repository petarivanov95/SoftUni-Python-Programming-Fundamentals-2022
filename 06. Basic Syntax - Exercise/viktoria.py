number_of_orders = int(input())
profit = 0

for order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    price = price_per_capsule * capsules_count * days
    profit += price

    if profit != 0:
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${profit:.2f}")
