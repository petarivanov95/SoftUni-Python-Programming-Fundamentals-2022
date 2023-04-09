intake = input().split(" ")
my_dict = {}

# option 1
for x in range(len(intake)):
    if x % 2 == 0:
        my_dict[intake[x]] = int(intake[x + 1])

print(my_dict)


# option 2


# # Loop through the input elements in pairs and add them to the dictionary
# for i in range(0, len(intake), 2):
#     key = intake[i]
#     value = int(intake[i+1])
#     my_dict[key] = value

# # Print the dictionary
# print(my_dict)


# sample input
# bread 10 butter 4 sugar 9 jam 12
