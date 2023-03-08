country_names = input().split(", ")
capital_cities = input().split(", ")

my_dict = dict(zip(country_names, capital_cities))

for x, y in my_dict.items():
    print(f"{x} -> {y}")
