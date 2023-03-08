coming_int = int(input())
not_divisiors = []
for x in range(2, coming_int):
    if coming_int % x != 0:
        not_divisiors.append(x)
    else:
        print("False")
        break

if len(not_divisiors) == len(list(range(2, coming_int))):
    print("True")
