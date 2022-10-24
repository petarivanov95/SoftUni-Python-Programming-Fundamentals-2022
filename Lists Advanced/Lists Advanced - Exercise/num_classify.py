nums_all = input().split(', ')
positives = [item for item in nums_all if int(item) >= 0]
negatives = [item for item in nums_all if int(item) < 0]
evens = [item for item in nums_all if int(item) % 2 == 0]
odds = [item for item in nums_all if int(item) % 2 != 0]

print(f"Positive: {', '.join(positives)}")
print(f"Negative: {', '.join(negatives)}")
print(f"Even: {', '.join(evens)}")
print(f"Odd: {', '.join(odds)}")
