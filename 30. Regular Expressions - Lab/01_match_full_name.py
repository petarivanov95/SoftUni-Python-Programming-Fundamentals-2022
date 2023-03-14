import re

# text = 'Peter Smith, peter smith, Peter smith, peter Smith, PEter Smith, Peter SmIth, Lily Everett'
text = input()
pattern = re.compile(r"\b[A-Z][a-z]{1,} [A-Z][a-z]{1,}\b")


matches = pattern.findall(text)

print(' '.join(matches))