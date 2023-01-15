orders = {}

while True:
    current_input = input()
    if current_input == 'buy':
        break
    name, price, qty = current_input.split(' ')
    if name not in orders:
        orders[name] = [float(price),int(qty)]
    else:
        orders[name][0] = float(price)
        orders[name][1] += int(qty)

for name in orders:
    total_price = orders[name][0] * orders[name][1] 
    print(f"{name} -> {total_price:.2f}")

# current_input = "Beer 2.20 100"
# name, price, qty = current_input.split(' ')
# if name not in orders:
#         orders[name] = [price,qty]

# orders[name] = [float(price),int(qty)]

# print(orders[name][0])
# # print(name, type(name))
# # print(price, type(price))
# # print(qty, type(qty))
