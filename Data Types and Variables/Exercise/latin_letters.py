my_num = int(input())

for x in range(97,97+my_num):
    for y in range(97,97+my_num):
        for z in range(97,97+my_num):
            print(f'{chr(x)}{chr(y)}{chr(z)}')

