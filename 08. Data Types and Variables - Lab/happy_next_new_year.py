year = int(input())
my_set = set()
year += 1
while True:
    my_set = set(list(str(year)))
    if len(my_set) == 4:
        print(year)
        break
    else:
        year += 1
