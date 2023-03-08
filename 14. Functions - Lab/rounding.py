import math

my_input = input().split(" ")


def rounder(lst):
    y = [round(float(x)) for x in lst]
    return y


print(rounder(my_input))
