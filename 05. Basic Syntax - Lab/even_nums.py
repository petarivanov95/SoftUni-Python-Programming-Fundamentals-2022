from itertools import count


lines = int(input())
counter = 0
for x in range(lines):
    new_num = int(input())
    if new_num%2 ==0:
        counter += 1
    else:
        print(f'{new_num} is odd!')
        break

if counter == lines:
    print('All numbers are even.')

