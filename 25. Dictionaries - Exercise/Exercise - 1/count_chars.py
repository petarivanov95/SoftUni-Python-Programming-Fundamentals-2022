input_str = input()
my_dict = {}

for x in input_str:
    # if x == ' ':
    #     pass
    if x in my_dict:
        my_dict[x] += 1
    else:
        my_dict[x] = 1

for char in my_dict:
    if char == " ":
        break
    print(f"{char} -> {my_dict[char]}")
