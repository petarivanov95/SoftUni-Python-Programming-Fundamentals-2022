def chars(x,y):
    the_lst = [chr(a) for a in range(ord(x)+1,ord(y))]
    return ' '.join(the_lst)

input_1 = input()
input_2 = input()

print(chars(input_1,input_2))
