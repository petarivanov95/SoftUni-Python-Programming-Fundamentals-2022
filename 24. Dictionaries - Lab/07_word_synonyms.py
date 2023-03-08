count = int(input())
my_dict = {}

for x in range(count):
    word = input()
    meaning = input()

    if word in my_dict:
        my_dict[word].append(meaning)
    else:
        my_dict[word] = []
        my_dict[word].append(meaning)


for word in my_dict:
    print(f'{word} - {", ".join(my_dict[word])}')
