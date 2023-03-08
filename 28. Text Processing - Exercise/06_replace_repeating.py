sequence = list(input())
unique = []

for idx, char in enumerate(sequence):
    if len(unique) == 0:
        unique.append(char)
    else:
        if char == unique[-1]:
            pass
        else:
            unique.append(char)
print("".join(unique))


