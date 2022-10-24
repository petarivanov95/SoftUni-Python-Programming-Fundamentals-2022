employees = input().split()
factor = int(input())

employees = list(map(lambda x: int(x)*factor, employees))

filtered = list(filter(lambda x: x >= (sum(employees)/len(employees)),employees))

if len(filtered) >= len(employees)/2:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are not happy! ')

my_list = [-1,2,-3,4,5]
factor = 3
new_list = list(map(lambda x: factor*x ,my_list))

print(my_list)
print(new_list)