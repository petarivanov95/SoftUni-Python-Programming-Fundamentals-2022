my_number = float(input())

if my_number == 0:
    print('zero')
elif my_number > 0:
    if abs(my_number) < 1: 
        print('small positive')
    elif my_number > 1_000_000:
        print('large positive')
    else:
        print('positive')
else:
    if abs(my_number) < 1:
        print('small negative')
    elif my_number < -1_000_000:
        print('large negative')
    else:
        print('negative')


