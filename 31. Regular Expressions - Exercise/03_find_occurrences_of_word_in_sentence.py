import re

line = input()
word = input()
results = []

search_pattern = rf"\b{word}\b"
result = re.finditer(search_pattern, line,flags = re.IGNORECASE)

for x in result:

    results.append(x)

print(len(results))
