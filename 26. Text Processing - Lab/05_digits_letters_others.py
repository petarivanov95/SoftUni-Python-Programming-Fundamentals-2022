the_string = input()
digits = "".join([x for x in the_string if x.isnumeric()])
alphabet = "".join([x for x in the_string if x.isalpha()])
chars = "".join([x for x in the_string if not x.isalpha() and not x.isnumeric()])

print(f"{digits}")
print(f"{alphabet}")
print(f"{chars}")
