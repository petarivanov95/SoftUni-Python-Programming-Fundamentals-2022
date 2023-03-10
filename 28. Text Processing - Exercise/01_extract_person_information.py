num_lines = int(input())
inputs_strings = [input() for _ in range(num_lines)]

for sentence in inputs_strings:
    name = ''
    age = ''
    start_name = 0
    end_name = 0
    end_age = 0
    start_age = 0
    
    for id, char in enumerate(sentence):
        if char == "@":
            start_name = id + 1
        elif char == "|":
            end_name = id
        elif char == "#":
            start_age = id + 1
        elif char == "*": 
            end_age = id
          
    name = sentence[start_name:end_name]
    age = sentence[start_age:end_age]
    print(f"{name} is {int(age)} years old.") 
        
# sample input 
# 3
# random name @lilly| random digits #5*age
# @Marry| with age #19*
# here Comes @Garry|he is #48* years old