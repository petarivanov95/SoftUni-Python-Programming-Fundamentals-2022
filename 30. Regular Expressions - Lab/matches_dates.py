import re

pattern = re.compile(r'(\d{2})([\/\-\.])([A-Z][a-z]{2})\2(\d{4})')

text = input()

results = pattern.finditer(text)

for result in results:
    print(f"Day: {result.group(1)}, Month: {result.group(3)}, Year: {result.group(4)}")

