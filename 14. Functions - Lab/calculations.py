def calculator(operator, x, y):
    if operator == "add":
        return x + y
    elif operator == "subtract":
        return x - y
    elif operator == "multiply":
        return x * y
    elif operator == "divide":
        return int(x / y)


operator_argument = input()
first_num = int(input())
second_num = int(input())

print(calculator(operator_argument, first_num, second_num))
