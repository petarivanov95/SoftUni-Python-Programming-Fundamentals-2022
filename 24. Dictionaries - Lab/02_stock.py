my_stock_list = input().split(' ')
lst_len = len(my_stock_list)

my_stock_dict = {my_stock_list[x]:int(my_stock_list[x+1]) for x in range(lst_len) if x%2==0}

# Create the stock dictionary from user input
# my_stock_dict = {}
# for i in range(0, len(my_stock_list), 2):
#     key = my_stock_list[i]
#     value = int(my_stock_list[i+1])
#     my_stock_dict[key] = value


checker = input().split(' ')

for item in range(len(checker)):
    product = checker[item]
    if checker[item] in my_stock_dict:
        quantity = my_stock_dict[checker[item]]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")