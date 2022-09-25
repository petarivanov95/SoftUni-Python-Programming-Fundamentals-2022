num = input()
my_list = []

for x in num:
    my_list.append(x)
my_list.sort(reverse=True)
print(''.join(my_list))