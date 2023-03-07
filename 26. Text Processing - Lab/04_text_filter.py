ban_list = input().split(', ')
text = input()

for word in ban_list:
    while True:
        if word in text:
            text = text.replace(word, '*'*len(word))
        else:
            break

print(text)