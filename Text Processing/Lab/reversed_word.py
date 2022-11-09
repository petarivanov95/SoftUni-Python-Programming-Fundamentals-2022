## method 1
# command = input()

# while command != 'end':
#     word_list = [x for x in command]
#     word = ''.join(word_list)
#     reversed_word = ''.join(word_list[::-1])
#     print(f"{word} = {reversed_word}")
#     command = input()

# # method 2
# command = input()

# while command != 'end':
#     word_list = [x for x in command]
#     word = ''.join(word_list)
#     reversed_word = ''.join(reversed(word_list))
#     print(f"{word} = {reversed_word}")
#     command = input()



# method 3
command = input()

while command != 'end':
    reversed_word = ''.join(list(command)[::-1])
    print(f"{command} = {reversed_word}")
    command = input()
