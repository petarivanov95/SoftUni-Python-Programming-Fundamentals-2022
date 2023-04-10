import re

while True:
    message = input()
    if message == "Last note":
        break

    pattern = r"^(?P<name>[A-Za-z0-9!@#$\?]+)=(?P<length>\d+)<<(?P<code>.+)$"
    match = re.match(pattern, message)

    if match:
        name = match.group("name")
        length = int(match.group("length"))
        code = match.group("code")

        if length == len(code):
            name = re.sub("[^A-Za-z0-9]+", "", name)
            print(f"Coordinates found! {name} -> {code}")
        else:
            print("Nothing found!")
    else:
        print("Nothing found!")

# import re
#
# while True:
#     message = input()
#     if message == "Last note":
#         break
#     pattern = r"^(?P<name>[A-Za-z0-9!@#$?]+)=\d+<<(?P<code>[^<>]+)$"
#     match = re.match(pattern, message)
#     if match:
#         name = match.group("name")
#         code = match.group("code")
#         length = int(message.split("=")[1].split("<<")[0])
#         if len(code) == length:
#             print(f"Coordinates found! {name} -> {code}")
#         else:
#             print("Nothing found!")
#     else:
#         print("Nothing found!")
