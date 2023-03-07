# # method 1

# my_str = input()
# list_of_str = my_str.split(' ')
# resulting_strings = []
# for word in list_of_str:
#     resulting_strings.append(word*len(word))

# print(''.join(resulting_strings))

# method 2

input_strings = input().split(' ')
resulting_strings = [word*len(word) for word in input_strings]
print(''.join(resulting_strings))