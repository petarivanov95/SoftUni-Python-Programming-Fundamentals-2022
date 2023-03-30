
command = input()
idx = 1
contest_data = {}
user_point_data = {}


while True:
    if command == 'no more time':
        break
    else:
        username, contest, points = command.split(' -> ')
        
        if contest in contest_data.keys():
            if username in contest_data[contest].keys():
                if contest_data[contest][username] < points:
                    contest_data[contest][username] = points
            else:
                contest_data[contest][username] = points
        else:
            contest_data[contest] = {username:points}
                        
    command = input()
        
for contest, user_info in contest_data.items():
    print(f"{contest}: {len(user_info)} participants")
    for user,points in user_info.items():
        if user in user_point_data.keys():
            user_point_data[user] += int(points)
        else:
            user_point_data[user] = int(points)
        print(f"{idx}. {user} <::> {points}")
        idx += 1
        
print('Individual standings')
sortedDict = sorted(user_point_data.items(), key = lambda x: x[1], reverse = True)
for idx, item in enumerate(sortedDict):
    print(f"{idx + 1}. {item[0]} -> {item[1]}")
    
    

        

        
# test_dict = {'Algo':{'Peter':100, 'George':200}}
# print(test_dict['Algo'])
# print(test_dict['Algo'].keys())
# # print(test_dict['Algo'])


