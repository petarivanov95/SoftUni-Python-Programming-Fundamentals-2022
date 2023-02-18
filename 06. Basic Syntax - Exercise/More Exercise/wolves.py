flock = input().split(', ')

if flock[-1] == 'wolf':
    print("Please go away and stop eating my sheep")
else:
    for id, item in enumerate(flock):
        if item == 'wolf':
            n = len(flock)-id-1
            print(f"Oi! Sheep number {n}! You are about to be eaten by a wolf!")