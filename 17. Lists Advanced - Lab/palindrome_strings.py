words = input()
palindrome = input()
palindromes = []
word_list = words.split()

for x in range(len(word_list)):
    if word_list[x] == "".join(reversed(word_list[x])):
        palindromes.append(word_list[x])

counter = 0
for x in range(len(palindromes)):
    if palindromes[x] == palindrome:
        counter += 1
print(palindromes)
print(f"Found palindrome {counter} times")
