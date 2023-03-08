new_num = int(input())

for x in range(new_num):
    my_string = input()
    if "." in my_string or "," in my_string or "_" in my_string:
        print(f"{my_string} is not pure!")
    else:
        print(f"{my_string} is pure.")
