n = int(input())
register = {}
for command in range(n):
    user_input = input().split()

    if  'register' in user_input:
        command, username, license_plate_number = user_input
        if username not in register:
            register[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    elif 'unregister' in user_input:
        command, username = user_input
        if username not in register:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del register[username]


for username, license_plate_number in register.items():
    print(f'{username} => {license_plate_number}')