lines = int(input())
sum_var = 0
for x in range(lines):
    new_entry = ord(input())
    sum_var += new_entry

print(f'The sum equals: {sum_var}')