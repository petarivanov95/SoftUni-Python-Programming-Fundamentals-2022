import re

line = input()
results = []

search_pattern = r"(\s_)([a-zA-Z0-9]+\b)"
result = re.finditer(search_pattern, line)

for x in result:
    # print(x)
    results.append(x.group(2))

# print(results)
print(','.join(results))