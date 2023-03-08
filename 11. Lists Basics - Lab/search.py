lines = int(input())
code_word = input()
my_lst = []
new_lst = []
for x in range(lines):
    new_str = input()
    my_lst.append(new_str)
print(my_lst)

for x in range(len(my_lst)):
    if code_word in my_lst[x]:
        new_lst.append(my_lst[x])
print(new_lst)
