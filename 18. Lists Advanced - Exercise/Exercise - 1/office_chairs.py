num_rooms = int(input())
free_chairs = 0
extra_chairs_needed = 0

for room in range(1, num_rooms + 1):
    chairs_and_people = input().split(" ")

    difference = len(chairs_and_people[0]) - int(chairs_and_people[1])

    if len(chairs_and_people[0]) > int(chairs_and_people[1]):
        free_chairs += abs(difference)
    elif len(chairs_and_people[0]) == int(chairs_and_people[1]):
        continue
    elif len(chairs_and_people[0]) < int(chairs_and_people[1]):
        print(f"{abs(difference)} more chairs needed in room {room}")
        extra_chairs_needed += abs(difference)


if free_chairs != 0 and free_chairs > extra_chairs_needed:
    print(f"Game On, {abs(free_chairs)} free chairs left")
