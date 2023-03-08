people = int(input())
capacity = int(input())

trips = people // capacity
leftover = people % capacity

if people < capacity:
    print("1")
elif people % capacity == 0:
    print(trips)
else:
    print(trips + 1)
