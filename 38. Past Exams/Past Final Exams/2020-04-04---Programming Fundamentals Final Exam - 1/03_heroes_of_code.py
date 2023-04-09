def cast_spell(heroes, hero_name, mp_needed, spell_name):
    hero = heroes[hero_name]
    if hero['mp'] >= mp_needed:
        hero['mp'] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {hero['mp']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")


def take_damage(heroes, hero_name, damage, attacker):
    hero = heroes[hero_name]
    hero['hp'] = max(0, hero['hp'] - damage)
    if hero['hp'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero['hp']} HP left!")
    else:
        del heroes[hero_name]
        print(f"{hero_name} has been killed by {attacker}!")


def recharge(heroes, hero_name, amount):
    hero = heroes[hero_name]
    hero['mp'] = min(200, hero['mp'] + amount)
    print(f"{hero_name} recharged for {hero['mp'] - (hero['mp'] - amount)} MP!")


def heal(heroes, hero_name, amount):
    hero = heroes[hero_name]
    hero['hp'] = min(100, hero['hp'] + amount)
    print(f"{hero_name} healed for {hero['hp'] - (hero['hp'] - amount)} HP!")


def display_heroes(heroes):
    for hero_name, hero in heroes.items():
        print(f"{hero_name}\n  HP: {hero['hp']}\n  MP: {hero['mp']}")


n = int(input())
heroes = {}

for i in range(n):
    name, hp, mp = input().split()
    heroes[name] = {'hp': int(hp), 'mp': int(mp)}

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split(" - ")
    action = tokens[0]
    hero_name = tokens[1]

    if action == "CastSpell":
        mp_needed = int(tokens[2])
        spell_name = tokens[3]
        cast_spell(heroes, hero_name, mp_needed, spell_name)
    elif action == "TakeDamage":
        damage = int(tokens[2])
        attacker = tokens[3]
        take_damage(heroes, hero_name, damage, attacker)
    elif action == "Recharge":
        amount = int(tokens[2])
        recharge(heroes, hero_name, amount)
    elif action == "Heal":
        amount = int(tokens[2])
        heal(heroes, hero_name, amount)

display_heroes(heroes)
