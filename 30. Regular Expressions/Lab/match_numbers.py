import re

pattern = re.compile(r'(^|(?<=\s))\-?([0]|[1-9][0-9]*)(\.\d+?)?($|(?=\s))')

text = input()
  
results = pattern.finditer(text)


for result in results:
    print(result.group(),end=' ')