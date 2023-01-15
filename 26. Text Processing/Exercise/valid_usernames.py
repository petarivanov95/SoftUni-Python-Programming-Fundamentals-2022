# usernames = input().split(', ')
# valid = []
# valid_chars = '_-'
# for name in usernames:
#     chars_in_name = list(name)
#     invalid_syms = []
#     if 3<=len(name)<=16:
#         for chr in chars_in_name:
#             if chr in valid_chars:
#                 pass
#             elif chr.isnumeric():
#                 pass
#             elif chr.isalpha():
#                 pass
#             else:
#                 invalid_syms.append(chr)
            
#         if len(invalid_syms) > 0:
#             continue
#         else:
#             valid.append(name)

# for name in valid:
#     print(name)


 
def length_is_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False
 
 
def characters_are_valid(name):
    for character in name:
        if not (character.isalnum() or character == "_" or character == "-"):
            return False
    return True
 
 
def no_redundant_symbols_(name):
    if ' ' in name:
        return False
    return True
 
 
def username_validation(name):
    if length_is_valid(name) and characters_are_valid(name) and no_redundant_symbols_(name):
        return True
    return False
 
 
usernames = input().split(", ")
for username in usernames:
    if username_validation(username):
        print(username)
 
 
 
 