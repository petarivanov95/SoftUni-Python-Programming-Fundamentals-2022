num = input()
my_list = []

# loop through all digits of the num and add to a list
for x in num:
    my_list.append(x)

my_list.sort(reverse=True)  # sort all the digits in descending order
print("".join(my_list))  # joining the ordered digits yields the largest num possible
