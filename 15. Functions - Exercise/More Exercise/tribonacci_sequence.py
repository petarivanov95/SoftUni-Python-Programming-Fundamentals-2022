input_num = int(input())

def tribonacci(num):
    nums = [1,1,2]
    counter = 3
    for _ in range(num):
        if num == 3:
            return nums
        else:
            while counter < num:
                new_num = nums[-1]+nums[-2]+nums[-3]
                nums.append(new_num)
                counter+=1
    return nums


the_nums = tribonacci(input_num)
for x in the_nums:
    print(x,end=' ')

