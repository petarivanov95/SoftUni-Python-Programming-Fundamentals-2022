# my_to_do = []
# command = ''

# while command != 'End':
#     command = input()
#     command_list = command.split('-')
#     if command == 'End':
#         break
#     else:
#         priority = int(command_list[0])
#         task = command_list[-1]
#         my_to_do.append((priority,task))

# # sorted_tasks = [task[1] for task in sorted(my_to_do)]
# # print(sorted_tasks)
# print(sorted(my_to_do))

my_to_do = []
command = ''

while command != 'End':
    command = input()
    command_list = command.split('-')
    if command == 'End':
        break
    else:
        # priority = int(command_list[0])
        # task = command_list[-1]
        my_to_do.append((command_list[0],command_list[-1]))


print(sorted(my_to_do, key = lambda x: x[0]))
sorted_tasks = [task[1] for task in sorted(my_to_do)]
print(sorted_tasks)