input_lst = [int(x) for x in input().split(', ')]

new_lst = []
zeros = []
for id,x in enumerate(input_lst):
    if x == 0:
        zeros.append(x)
    else:
        new_lst.append(x)

new_lst.extend(zeros)

print(new_lst)