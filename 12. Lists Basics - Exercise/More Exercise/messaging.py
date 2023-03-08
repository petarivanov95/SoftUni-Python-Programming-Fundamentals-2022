sequence = input().split(" ")
sentence = input()

indexes = []
for num in sequence:
    digits = [int(x) for x in list(num)]
    idx = sum(digits)
    indexes.append(idx)

message = ""

for index in indexes:
    if index > len(sentence):
        id = index - len(sentence)
        message += sentence[id]
        sentence = sentence[:id] + sentence[id + 1 :]

    elif index < len(sentence):
        message += sentence[index]
        sentence = sentence[:index] + sentence[index + 1 :]

print(message)

# index = 1
# sentence = 'This is some message for you'
# print(sentence)
# sentence = sentence[:index]+sentence[index+1:]
# print(sentence)
