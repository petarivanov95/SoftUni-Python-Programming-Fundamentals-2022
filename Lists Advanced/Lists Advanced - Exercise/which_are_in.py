# seq1 = input().split(', ')
# seq2 = input().split(', ')

# in_both = set()

# for x in seq1:
#     for y in seq2:
#         if x in y:
#             in_both.add(x)

# print(list(in_both))

seq1 = input().split(', ')
seq2 = input().split(', ')

in_both = []

for x in seq1:
    for y in seq2:
        if x in y and x not in in_both:
            in_both.append(x)

print(in_both)