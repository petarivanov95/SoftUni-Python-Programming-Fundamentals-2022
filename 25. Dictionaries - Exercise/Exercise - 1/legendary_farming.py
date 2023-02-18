# # trinkets = {
# # "Shadowmourne":[250, 'shards'],
# # "Valanyr": [250,'fragments'], 
# # 'Dragonwrath' :[250, 'motes']
# # }

current = {'shards':0,'fragments':0, 'motes':0}
obtained = False
received_items = input().split()

while not obtained:
    for index in range(0,len(received_items),2):
        value = int(received_items[index])
        key = received_items[index+1].lower()

        if key not in current.keys():
            current[key] = 0
        current[key] += value

        if current['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            current['shards'] -= 250
            obtained = True
        elif current['fragments'] >= 250:
            print(f'Valanyr obtained!')
            current['fragments'] -= 250
            obtained = True
        elif current['motes'] >= 250:
            print(f'Dragonwrath obtained!')
            current['motes'] -= 250
            obtained = True

        if obtained:
            break
    if obtained:
        break
    received_items = input().split()
    

for key,value in current.items():
    print(f"{key}: {value}") 

# items = {"shards": 0, "fragments": 0, "motes": 0}
# current_items = input().split()
# obtained = False
# print(current_items)
# while not obtained:
#     for index in range(0, len(current_items), 2):
#         value = int(current_items[index])
#         key = current_items[index + 1].lower()
#         if key not in items.keys():
#             items[key] = 0
#         items[key] += value
#         if items["shards"] >= 250:
#             print("Shadowmourne obtained!")
#             items["shards"] -= 250
#             obtained = True
#         elif items["fragments"] >= 250:
#             print("Valanyr obtained!")
#             items["fragments"] -= 250
#             obtained = True
#         elif items["motes"] >= 250:
#             print("Dragonwrath obtained!")
#             items["motes"] -= 250
#             obtained = True
#         if obtained:
#             break
#     if obtained:
#         break
#     current_items = input().split()
# for material, quantity in items.items():
#     print(f"{material}: {quantity}")