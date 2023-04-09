import functools
import re

line = input()
results = []

nums_pattern = r"(\d+)"
nums_found = re.findall(nums_pattern, line)
nums_ints = [list(x) for x in nums_found]

all_digits = []
for a_list in nums_ints:
    for num in a_list:
        all_digits.append(int(num))

product = functools.reduce(lambda a, b: a  *b, all_digits)

search_pattern = r"(:{2}|\*{2})([A-Z][a-zA-Z]{2,})(\1)"
result = re.finditer(search_pattern, line)
results_strs_only = []

dict_emojis = {}

for x in result:
    dict_emojis[x.group(2)] = [0, x.group()]

for result in dict_emojis:
    tmp_num = 0
    for x in list(result):
        tmp_num += ord(x)

    dict_emojis[result][0] += tmp_num

print(f"Cool threshold: {product}")
print(f"{len(dict_emojis)} emojis found in the text. The cool ones are:")
for k, v in dict_emojis.items():
    if v[0] > product:
        print(f"{v[1]}")