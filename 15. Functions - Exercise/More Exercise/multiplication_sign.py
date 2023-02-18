
input_num_1 = int(input())
input_num_2 = int(input())
input_num_3 = int(input())

def sign_checker(a,b,c):
    pos = 0
    zero = 0
    neg = 0
    the_list = [a,b,c]
    for x in the_list:
        if x > 0:
            pos += 1
        elif x == 0:
            zero += 1
        else:
            neg += 1


    if zero > 0:
        return 'zero'
    else:
        if neg % 2 == 0:
            return 'positive'
        else:
            return 'negative'

print(sign_checker(input_num_1,input_num_2,input_num_3))


        
