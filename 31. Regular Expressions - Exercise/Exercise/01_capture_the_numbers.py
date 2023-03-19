import re

line = input()
results = []

while line:
    search_pattern = r"\d+"
    result = re.findall(search_pattern, line)
    for x in result:
        results.append(x)
    line = input()


print(' '.join(results))