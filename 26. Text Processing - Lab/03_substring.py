first_str = input()
second_str = input()

## method 1
# while True:
#     if first_str in second_str:
#         result = second_str.index(first_str)
#         new = second_str[:result]+second_str[result+len(first_str):]
#         second_str = new
#     else:
#         print(second_str)
#         break

# method 2
while first_str in second_str:
    second_str = second_str.replace(first_str, "")
print(second_str)
