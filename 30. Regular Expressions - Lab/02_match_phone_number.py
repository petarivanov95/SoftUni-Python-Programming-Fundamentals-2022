import re

text = input()
pattern = r'\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b'
# pattern = r'\+359( |-)2(\1)\d{3}(\1)\d{4}\b'

matches = re.findall(pattern, text)

print(matches)