import re

# text = 'Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett'
text = input()
pattern =re.compile(r'(\b[A-Z][a-z]+) ([A-Z][a-z]+\b)')

matches = pattern.findall(text)

for match in matches:
    print(f'{" ".join(match)}',end=', ')