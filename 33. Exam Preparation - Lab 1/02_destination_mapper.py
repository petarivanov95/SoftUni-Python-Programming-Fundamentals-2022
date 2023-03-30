# Python solution

import re

string = input()

valid_locations = re.findall(r"([=/])([A-Z][a-zA-Z]{2,})\1", string)

travel_points = sum(len(location[1]) for location in valid_locations)

valid_locations = [location[1] for location in valid_locations]

print(f"Destinations: {', '.join(valid_locations)}")
print(f"Travel Points: {travel_points}")
