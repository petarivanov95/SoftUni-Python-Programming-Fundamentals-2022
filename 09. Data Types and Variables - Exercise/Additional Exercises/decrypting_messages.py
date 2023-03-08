my_key = int(input())
num_lines = int(input())
letters = []

for x in range(num_lines):
    letter = input()
    letters.append(ord(letter) + my_key)

new_letters = []
for letter in letters:
    new_letters.append(chr(letter))

word = "".join(new_letters)
print(word)
