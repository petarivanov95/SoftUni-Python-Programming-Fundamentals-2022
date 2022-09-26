num = int(input())
num_list = list(range(1,num+1))
special_nums = [5,7,11]

for x in range(1, num+1):
    sum = 0
    for digit in str(x): 
      sum += int(digit)
    if sum in special_nums:
        print(f'{x} -> True')
    else:
        print(f'{x} -> False')