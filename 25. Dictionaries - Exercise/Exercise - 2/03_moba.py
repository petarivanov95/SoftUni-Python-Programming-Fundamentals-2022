END_CONDITION = 'Season end'
command = input()
players_info = {}

while True:
    if command == END_CONDITION:
        break
    else:
        if '->' in command:
            player, position, skill = command.split(' -> ')
            skill = int(skill)
            if player in players_info:
                if position in players_info[player]:
                    if skill > players_info[player][position]:
                        players_info[player][position] = skill
                else:
                    players_info[player][position] = skill
            else:
                players_info[player] = {position: skill}
        else:
            # duel here
            pass

    command = input()
print(players_info)
