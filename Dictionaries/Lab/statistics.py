products = {}
while True:
    command = input()
    if command == 'statistics':
        break
    else:
        key, value = command.split(': ')
        if key in products:
            products[key] += int(value)
        else:
            products[key] = int(value)

print('Products in stock:')
for key,value in products.items():
    print(f'- {key}: {value}')

count_all_products = len(products)
sum_all_quantities = sum(products.values())

print(f'Total Products: {count_all_products}')
print(f'Total Quantity: {sum_all_quantities}')
