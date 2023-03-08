all_names = input().split(", ")

my_func = lambda x: (-len(x), x)
sorted_list = sorted(all_names, key=my_func)


print(sorted_list)
