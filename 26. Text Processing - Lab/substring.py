first = input()
second = input()

while True:
    if first in second:
        result = second.index(first)
        new = second[:result]+second[result+len(first):]
        second = new
    else:
        print(second)
        break