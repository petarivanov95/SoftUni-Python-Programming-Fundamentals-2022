import re

n = int(input())

for i in range(n):
    barcode = input()
    valid = True
    product_group = ""

    if barcode[0] != "@" or barcode[-1] != "@":
        valid = False
    else:
        if len(barcode) < 6:
            valid = False
        else:
            pattern = r"@#+[A-Z][A-Za-z0-9]*[A-Z]@#+"
            if not re.match(pattern, barcode):
                valid = False
            else:
                for char in barcode:
                    if char.isdigit():
                        product_group += char
                if product_group == "":
                    product_group = "00"

    if valid:
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")


