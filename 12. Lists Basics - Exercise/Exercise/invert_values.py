string_val = input()
string_list = string_val.split()
opposite_values_list = [-1 * int(x) for x in string_list]
print(opposite_values_list)
