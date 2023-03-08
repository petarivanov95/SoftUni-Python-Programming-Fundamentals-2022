import math

numbers = input().split(", ")
number_lst = []
group_of_ten = 10
while len(numbers) > 0:
    for current_number in numbers:
        if int(current_number) <= group_of_ten:
            number_lst.append(current_number)
            numbers.remove(current_number)

    print(f"Group of {group_of_ten}'s: {' '.join(number_lst)}")
    group_of_ten += 10
    number_lst = []
