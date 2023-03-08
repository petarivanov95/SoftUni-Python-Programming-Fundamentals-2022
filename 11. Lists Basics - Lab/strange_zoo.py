initial_positioning = []

for x in range(3):
    part = input()
    initial_positioning.append(part)

initial_positioning[0], initial_positioning[2] = (
    initial_positioning[2],
    initial_positioning[0],
)

print(initial_positioning)
