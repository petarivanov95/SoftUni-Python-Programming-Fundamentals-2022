lines = int(input())
my_list = []

# this loop creates a list with the inputs
    input_str = input()
    my_list.append(input_str)


balanced = 0 # this variable will keep track of the balance

# this loop goes through the list and keeps track of parentheses balance
for y in my_list:
    if balanced < 0 or balanced > 1: # at each iteration checks balance
        break
    if len(y) > 1: # if string is longer than one char skip
        continue
    else:
        if ord(y) == 40: # 40 is the sign for '('
            balanced += 1
        elif ord(y) == 41: # 41 is the sign for ')'
            balanced -= 1
        else:
            continue

if balanced == 0:
    print ("BALANCED")
else:
    print('UNBALANCED')
