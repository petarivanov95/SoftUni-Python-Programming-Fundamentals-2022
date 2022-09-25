my_str = input()
my_lst = []

for x in my_str:
    my_lst.append(x)

lst_caps = []

for x in range(len(my_lst)):
    if my_lst[x].isupper():
        lst_caps.append(x)

print(lst_caps)