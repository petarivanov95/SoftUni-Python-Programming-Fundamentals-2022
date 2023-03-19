import re

line = input()
results = []

while line:
    search_pattern = r"([w]{3})\.([a-zA-Z0-9-]+)(\.[a-z]+)+"
    result = re.finditer(search_pattern, line)
    for x in result:
        results.append(x.group())
    line = input()

for result in results:
    print(result)

