import re

command = input().lower()
counter = 0
words = ["sand", "water", "fish", "sun"]

for word in words:
    for match in re.finditer(word, command):
        counter += 1


print(counter)
