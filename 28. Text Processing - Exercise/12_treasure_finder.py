# read keys input
keys = input().split(' ')

# initialize an empty list to store the input strings
strings = []

# continuously read input until 'find' is entered
while True:
    command = input()
    if command == 'find':
        break
    # add each input string to the list
    messcoords = command
    strings.append(messcoords)

# initialize an empty list to store the decrypted strings
decripted_strings = []

# loop over each string in the input list
for line in strings:
    new_str = ''
    # loop over each character in the string
    for id, char in enumerate(line):
        # decrypt the character by subtracting the corresponding key value
        new_str += chr(ord(char) - int(keys[id % len(keys)]))
    # add the decrypted string to the list
    decripted_strings.append(new_str)

# loop over each decrypted string in the list
for line in decripted_strings:
    # initialize some variables to store the type and coordinates
    type_ids = []
    coords_start = 0
    coords_end = 0
    # loop over each character in the string
    for id, char in enumerate(line):
        # if the character is '&', record its index
        if char == '&':
            type_ids.append(int(id))
        # if the character is '<', record its index
        elif char == '<':
            coords_start = int(id)
        # if the character is '>', record its index
        elif char == '>':
            coords_end = int(id)

    # extract the type and coordinates from the string
    the_type = line[type_ids[0] + 1 : type_ids[1]]
    coords = line[coords_start + 1 : coords_end]
    # print the result
    print(f"Found {the_type} at {coords}")
