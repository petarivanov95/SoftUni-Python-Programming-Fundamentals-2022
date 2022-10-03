a = [i for i in range(1,11+1)]
b = [y for y in range(1,11+1)]
cards = input()
lst = cards.split()
cards_list = [x.split() for x in lst]
print(cards_list)
# while True:

#     if 'A' in card.split():
#         a.pop(card.split()[-1])
#     elif 'B' in card.split():
#         b.pop(card.split()[-1])
#     else:
#         continue

#     if len(a) < 7:
#         break
#     if len(b) <7:
#         break

# print(f"Team A - {len(a)}; Team B - {len(b)}")