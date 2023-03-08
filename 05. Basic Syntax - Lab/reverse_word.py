word = input()
my_list = []
for letter in word:
    my_list.append(letter)

my_list.reverse()
print("".join(my_list))
