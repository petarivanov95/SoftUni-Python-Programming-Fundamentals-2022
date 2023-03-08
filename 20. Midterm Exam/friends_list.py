friends = input().split(", ")


def friends_processor(my_list):
    while True:
        command = input().split()

        if command[0] == "Report":
            break

        if command[0] == "Blacklist":
            if command[1] in my_list:
                special_val = my_list.index(command[1])
                print(f"{my_list[special_val]} was blacklisted.")
                my_list[special_val] = "Blacklisted"
            else:
                print(f"{command[1]} was not found.")

        elif command[0] == "Error":
            indx = int(command[1])
            if (
                0 <= indx < len(my_list)
                and my_list[indx] != "Blacklisted"
                and my_list[indx] != "Lost"
            ):
                print(f"{my_list[indx]} was lost due to an error.")
                my_list[indx] = "Lost"

        elif command[0] == "Change":
            indx = int(command[1])
            if 0 <= indx < len(my_list):
                print(f"{my_list[indx]} changed his username to {command[2]}.")
                my_list[indx] = command[2]

    blacklisted = my_list.count("Blacklisted")
    lost_names = my_list.count("Lost")
    final_list = " ".join(my_list)
    print(f"Blacklisted names: {blacklisted}")
    print(f"Lost names: {lost_names}")
    print(final_list)


friends_processor(friends)
