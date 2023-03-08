# sentence = input(). split(' ')

# for x in sentence:
#     if ':' in x:
#         print(x[:2])

# single_string = input()
# for index in range(len(single_string)):
#     # if single_string[index] == ":" and index != len(single_string) - 1:
#     if single_string[index] == ":":  
#         print(f":{single_string[index + 1]}")


single_string = list(input())

for index, letter in enumerate(single_string):
    if letter == ":":
        emoji = "".join(single_string[index:index + 2])
        print(f"{emoji}")
          
        