intake = input().split(' ')
my_dict = {}
for x in range(len(intake)):
    if x%2==0:
        my_dict[intake[x]] = int(intake[x+1])

print(my_dict)