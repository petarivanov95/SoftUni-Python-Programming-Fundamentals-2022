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
            player_one, player_two = command.split(" vs ")
            if player_one in players_info.keys() and player_two in players_info.keys():
                for position in players_info[player_one].keys():
                    if position in players_info[player_two].keys():
                        if sum(players_info[player_one].values()) > sum(players_info[player_two].values()):
                            del players_info[player_two]
                            break
                        elif sum(players_info[player_one].values()) < sum(players_info[player_two].values()):
                            del players_info[player_one]
                            break
                        else:
                            continue

    command = input()

print(players_info)
