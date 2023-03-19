import re

line = input()
results = []

search_pattern = r"\s([a-z0-9]+[a-z0-9\.\-\_]*@([a-z-]+)+(\.[a-z]+)+)\b"
result = re.finditer(search_pattern, line)

for x in result:
    print(x.group())

