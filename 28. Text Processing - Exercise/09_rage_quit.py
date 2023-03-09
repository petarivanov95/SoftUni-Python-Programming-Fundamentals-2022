# input_string = input()

# my_str = 'aSd2&5s@1'
# my_str = 'a3'

my_str = input()
new_str = ''
indexes = []

for id, value in enumerate(my_str):
    if value.isnumeric():
        indexes.append(id)

for id, value in enumerate(indexes):
    if id == 0:
        first = 0
    else:
        first = indexes[id - 1] + 1
    second = indexes[id]

    repeat = int(my_str[value])
    new_str += my_str[first:second].upper() * repeat


unique = set(new_str)

print(f"Unique symbols used: {len(unique)}")
print(new_str)

