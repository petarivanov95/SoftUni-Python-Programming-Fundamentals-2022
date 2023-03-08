def absolute_vals(n):
    x = [abs(float(y)) for y in n.split(" ")]
    return x


sequence = input()
print(absolute_vals(sequence))
