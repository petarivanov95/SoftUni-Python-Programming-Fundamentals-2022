int_1 = int(input())
int_2 = int(input())
my_lst = []
my_lst.append(int_1)
my_lst.append(int_2)

print('Before:')
print(f'a = {int_1}')
print(f'b = {int_2}')
print('After:')
int_1 = my_lst[1]
int_2 = my_lst[0]
print(f'a = {int_1}')
print(f'b = {int_2}')
