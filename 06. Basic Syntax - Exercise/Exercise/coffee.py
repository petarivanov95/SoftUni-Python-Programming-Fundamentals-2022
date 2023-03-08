code_words = ["coding", "dog", "cat", "movie"]
counter = 0
command = "1"
while command != "END":
    command = input()
    if command.lower() in code_words:
        if command.isupper():
            counter += 2
        else:
            counter += 1

if counter > 5:
    print("You need extra sleep")
else:
    print(counter)
