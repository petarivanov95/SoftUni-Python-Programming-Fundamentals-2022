
command = input()
cities = {}

while True:
    if command == "Sail":
        break
    city, population, gold = command.split('||')
    if city in cities:
        cities[city][0] += int(population)
        cities[city][1] += int(gold)
    else:
        cities[city] = [int(population), int(gold)]

    command = input()

command = input()

while True:
    commands = command.split("=>")
    if commands[0] == 'End':
        break

    elif commands[0] == 'Plunder':
        town = commands[1]
        people = commands[2]
        gold = commands[3]
        cities[town][0] -= int(people)
        cities[town][1] -= int(gold)
        if cities[town][0] <= 0 or cities[town][1] <= 0:
            del cities[town]
            print(f"{town} has been wiped off the map!")
        else:
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

    elif commands[0] == 'Prosper':
        town = commands[1]
        new_gold = int(commands[2])
        if new_gold < 0:
            print("Gold added cannot be a negative number!")
        cities[town][1] += int(new_gold)
        print(f"{new_gold} gold added to the city treasury. {town} now has {cities[town][1]} gold.")

    command = input()


if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, info in cities.items():
        print(f"{city} -> Population: {info[0]} citizens, Gold: {info[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

