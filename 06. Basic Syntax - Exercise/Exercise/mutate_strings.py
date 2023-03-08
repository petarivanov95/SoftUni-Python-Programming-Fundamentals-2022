# str_1 = input()
# str_2 = input()
# my_set = set()
# my_list = []
# for x in range(len(str_1)):
#     temp = str_2[0:x+1] + str_1[x+1:]
#     if temp in my_list:
#         continue
#     else:
#         print(temp)
#         my_list.append(temp)
#     # my_set.add(temp)
# #     # print(my_set)


# str_1 = input()
# str_2 = input()
# my_set = set()
# for x in range(len(str_1)):
#     temp = str_2[0:x+1] + str_1[x+1:]
#     if temp in my_set:
#         continue
#     else:
#         print(temp)
#         my_set.add(temp)
#     # my_set.add(temp)
#     # print(my_set)


str_1 = input()
str_2 = input()
last_str = str_1
for x in range(len(str_1)):
    temp = str_2[0 : x + 1] + str_1[x + 1 :]
    if temp == last_str:
        continue
    else:
        print(temp)
        last_str = temp
    # my_set.add(temp)
    # print(my_set)
