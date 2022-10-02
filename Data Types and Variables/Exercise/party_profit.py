group_size = int(input())
days_adventure = int(input())
coins_daily = 50
daily_food_person = 2
motivational_party = 3
boss_monster_per_person = 20
total_coins = 0

for x in range(1,days_adventure+1):
    if x % 10 == 0:
        group_size -= 2
    if x % 15 == 0:
        group_size += 5
    if x % 3 == 0:
        total_coins -= 3*group_size
    if x % 5 == 0:
        total_coins += 20*group_size
        if x % 3 == 0:
            total_coins -= 2*group_size

    total_coins += 50
    total_coins -= 2*group_size

print(f"{group_size} companions received {int(total_coins//group_size)} coins each.")