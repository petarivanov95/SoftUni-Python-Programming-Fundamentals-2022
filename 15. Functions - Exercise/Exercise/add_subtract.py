def sum_numbers(x, y):
    return x + y


def subtract(x, z):
    return x - z


a = int(input())
b = int(input())
c = int(input())

sum_func_result = sum_numbers(a, b)
subtract_func_result = subtract(sum_func_result, c)
print(subtract_func_result)
