num = int(input())


def sum_func(x):
    str_nums = list(str(x))
    even_digits = [int(a) for a in str_nums if int(a) % 2 == 0]
    odd_digits = [int(b) for b in str_nums if int(b) % 2 != 0]
    sum_of_even_digits = sum(even_digits)
    sum_of_odd_digits = sum(odd_digits)
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


print(sum_func(num))

# a = 1000435

# b = list(str(a))

# print(b)
