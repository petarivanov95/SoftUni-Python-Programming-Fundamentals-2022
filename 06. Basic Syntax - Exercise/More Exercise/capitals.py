# my_str = input()
my_lst = list(input())
lst_caps = []

# for x in my_str:
#     my_lst.append(x)


# for x in range(len(my_lst)): 
#     if my_lst[x].isupper():
#         lst_caps.append(x)

for id,item in enumerate(my_lst):
    if item.isupper():
        lst_caps.append(id)

print(lst_caps)