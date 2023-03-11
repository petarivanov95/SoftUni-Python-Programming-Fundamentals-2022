# print(ord('A')) 
# print(chr(73))
keys = input().split(' ')
strings = []

while True:
    command = input()
    if command == 'find':
        break
    messcoords = command
    strings.append(messcoords)

decripted_strings = []

for line in strings:
    new_str = ''
    for id, char in enumerate(line):
        new_str += chr(ord(char) - int(keys[id % len(keys)]))

    decripted_strings.append(new_str)


for line in decripted_strings:
    type_ids = []
    coords_start = 0
    coords_end = 0
    for id, char in enumerate(line):
        if char == '&':
            type_ids.append(int(id))
        elif char == '<':
            coords_start = int(id)
        elif char == '>':
            coords_end = int(id)


    the_type = line[type_ids[0] + 1 : type_ids[1]]
    coords = line[coords_start + 1 : coords_end]
    print(f"Found {the_type} at {coords}")
    


# keys = [1,2,1,3]

# for x in range(20):

#     print(keys[x % len(keys)])

