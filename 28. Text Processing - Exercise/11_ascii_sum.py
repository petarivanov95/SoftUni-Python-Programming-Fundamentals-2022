
char_1 = input()
char_2 = input()
random_string = input()

range_for_chars = [x for x in range(ord(char_1), ord(char_2) + 1)]
elements = []
for id, char in enumerate(random_string):
    if ord(char) in range_for_chars:
        elements.append(int(ord(char)))
        
print(sum(elements))