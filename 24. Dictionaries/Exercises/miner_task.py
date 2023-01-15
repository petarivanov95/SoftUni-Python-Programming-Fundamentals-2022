resources = {}
while True:

    command_1 = input()
    if command_1 == 'stop':
        break
    else:
        command_2 = input()
        if command_1 in resources:
            resources[command_1] += int(command_2)
        else:
            resources[command_1] = int(command_2)
    
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")