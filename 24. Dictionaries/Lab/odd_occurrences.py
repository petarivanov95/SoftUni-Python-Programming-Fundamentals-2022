sequence = input().split(' ')
my_dict = {}

for x in range(len(sequence)):
    if sequence[x].lower() in my_dict:
        my_dict[sequence[x].lower()] += 1
    else:
        my_dict[sequence[x].lower()] = 1


for word in my_dict:
    if not my_dict[word] % 2 == 0:
        print(word.lower(),end=' ')