characters = input().split(", ")

the_dict = {x: ord(x) for x in characters}

print(the_dict)
