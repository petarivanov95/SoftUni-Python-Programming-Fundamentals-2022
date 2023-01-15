divisor = int(input())
boundary = int(input())
max_num = 0

while True:
    if boundary%divisor == 0 and boundary >0:
        max_num = boundary
        break
    else:
        boundary -= 1
    
print(max_num)

