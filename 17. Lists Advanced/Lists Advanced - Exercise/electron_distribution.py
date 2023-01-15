
def electron_distribution(number):
    shell_base = 1 # minimum base number is 1
    full_shells = [] # place to store all shell positions as filled
    
    while True:
        shell_size = 2*(shell_base**2) # the size of the shell gets determined 
        if shell_size < number:
            full_shells.append(shell_size)
            number -= shell_size
        else:
            full_shells.append(number)
            break

        shell_base +=1

    return full_shells
num_electrons = int(input())
print(electron_distribution(num_electrons))

