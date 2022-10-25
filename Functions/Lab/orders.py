prices = {'coffee':1.50, 'water': 1.00, 'coke':1.40, 'snacks':2.00}

def calculator(menu, order, qty):
    if order in menu:
        price = menu[order]
        return price*qty

order_input = input()
quantity = int(input())
print(f"{calculator(prices,order_input,quantity):.2f}")