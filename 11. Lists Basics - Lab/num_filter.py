number = int(input())
all = []
evens = []
odds = []
positives = []
negatives = []
for x in range(number):
    new_int = int(input())
    all.append(new_int)

command = input()
if command == "even":
    for x in range(len(all)):
        if all[x] % 2 == 0 or all[x] == 0:
            evens.append(all[x])
    print(evens)
elif command == "odd":
    for x in range(len(all)):
        if all[x] % 2 != 0:
            evens.append(all[x])
    print(odds)
elif command == "positive":
    for x in range(len(all)):
        if all[x] >= 0:
            positives.append(all[x])
    print(positives)
elif command == "negative":
    for x in range(len(all)):
        if all[x] < 0:
            negatives.append(all[x])
    print(negatives)
