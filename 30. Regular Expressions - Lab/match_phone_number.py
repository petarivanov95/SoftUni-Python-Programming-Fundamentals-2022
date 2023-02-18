import re

text = input()
pattern = re.compile(r"[\+359]( |-)[2]\1\d{3}\b\1\d{4}\b")

matches = pattern.findall(text)

for match in matches:
    print(match)
