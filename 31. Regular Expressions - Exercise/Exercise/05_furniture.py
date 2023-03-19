import re

command = input()
total_cost = 0
furniture = {}

pattern = r"\>{2}([A-Z][A-Za-z]+)\<{2}([\d]+[\.]*[\d]+)\!([\d]+)"

while command != "Purchase":
    matches = re.finditer(pattern,command)
    for match in matches:
        name = match.group(1)
        price = match.group(2)
        quantity = match.group(3)

        furniture[name] = (price,quantity)

    command = input()

for k,v in furniture.items():
    price,qty = v 
    total_cost += float(price)*int(qty)

items = "\n".join(furniture.keys())
print(f'Bought furniture:\n{items}\nTotal money spend: {total_cost:.2f}')