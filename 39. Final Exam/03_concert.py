bands = {}
concert = {}
first_band = None

while True:
    command = input()
    if command == "Start!":
        break

    info = command.split("; ")
    action = info[0]
    band_name = info[1]

    if action == "Add":
        members = info[2].split(", ")
        if band_name not in bands:
            bands[band_name] = []
        for member in members:
            if member not in bands[band_name]:  # check for duplicates
                bands[band_name].append(member)

    elif action == "Play":
        time = int(info[2])
        if band_name not in concert:
            concert[band_name] = 0
            if first_band is None:  # assign first band to play
                first_band = band_name
        concert[band_name] += time

total_time = sum(concert.values())
print(f"Total time: {total_time}")

for band, time in concert.items():
    print(f"{band} -> {time}")

if first_band is not None:
    print(f"{first_band}")
    for member in bands[first_band]:
        print(f"=> {member}")
