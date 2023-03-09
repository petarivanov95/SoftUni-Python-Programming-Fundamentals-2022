

def exploder(a_string):
    strength = 0
    new_string = ""

    for idx, char in enumerate(a_string):
        
        # in each iteration, check whether the strength is greater 
        # than zero which will indicate that an explosion needs to happen 
        # this will be the case if there is no new mine. If there is no new mine
        # simply reduce the strength by 1 to indicate an explosion.
        if strength > 0 and char != ">":
            strength -= 1
        
        # if the character is a mine, add the strength of the subsequent character
        # to the overall strength but also make sure to add the character of the mine
        elif char == ">":
            strength += int(a_string[idx + 1])
            new_string += char
            
        # the third option is to not have a mine and not have an explosion
        # in which case the character is simply added to the new string    
        else:
            new_string += char
            
    return new_string

input_string = input()
print(exploder(input_string))

# sample = "abv>1>1>2>2asdasd"



# another method in progress 

# sample_list = list(sample)
# updated_list = sample_list[:]
# ids_to_remove = []
# mines = []
# mines_strength = []

# for id,x in enumerate(sample_list):
#     if x == ">":
#         mines.append(id)
#         mines_strength.append(int(sample_list[id+1]))

