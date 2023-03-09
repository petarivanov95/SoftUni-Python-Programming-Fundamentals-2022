inputs = input().split()
import string
lower_letters = dict(zip(string.ascii_lowercase, range(1,27)))
upper_letters = dict(zip(string.ascii_uppercase, range(1,27)))
total_sum = 0

for combo in inputs:
    result = 0
    if combo[0].isupper():
        result = int(combo[1:-1]) / upper_letters[combo[0]]
        
    elif combo[0].islower():
        result = int(combo[1:-1]) * lower_letters[combo[0]]
    
    if combo[-1].isupper():
        result -= upper_letters[combo[-1]]
        
    elif combo[-1].islower():
        result += lower_letters[combo[-1]]
        
    total_sum += result
    
print(f"{total_sum:.2f}")

# stra = 'A12b'

# print(stra[1:-1])