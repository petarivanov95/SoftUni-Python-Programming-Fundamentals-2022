command = input()

while command != 'end':
    word_list = [x for x in command]
    word = ''.join(word_list)
    reversed_word = ''.join(word_list[::-1])
    print(f"{word} = {reversed_word}")
    command = input()

