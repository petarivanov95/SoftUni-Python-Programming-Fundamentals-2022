vowels = ['a','e','o','u','i']

the_input = input()
my_filter = [x for x in the_input if x not in vowels]
print(''.join(my_filter))