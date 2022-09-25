num_orders = int(input())
total = 0
for x in range(num_orders):
    price_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_capsule < 0.01 or price_capsule > 100.00:
        continue
    elif days <1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day >2000:
        continue

    price = price_capsule*capsules_per_day*days
    total += price
    print(f'The price for the coffee is: ${price:.2f}')

print(f'Total: ${total:.2f}')