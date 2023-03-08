my_nums = input().split(", ")

indexes = [my_nums.index(x) for x in my_nums if int(x) % 2 == 0]
print(indexes)
