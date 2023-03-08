text = input().split(" ")

only_even_length = [word for word in text if len(word) % 2 == 0]

for x in only_even_length:
    print(x)
