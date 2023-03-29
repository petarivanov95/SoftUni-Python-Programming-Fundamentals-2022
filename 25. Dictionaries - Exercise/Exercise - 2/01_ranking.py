# Define end conditions for the two loops
END_CONDITION_CONTESTS = 'end of contests'
END_CONDITION_SUBMISSIONS = 'end of submissions'

# Initialize dictionaries to store contest data, passwords, and user points
contest_data = {}
contest_passwords = {}
user_points = {}

# Gather contest data and passwords from user input
command = input()
while command != END_CONDITION_CONTESTS:
    contest, password = command.split(':')
    contest_passwords[contest] = password
    command = input()

# Gather user submissions and update user points if the contest and password are valid
command = input()
while command != END_CONDITION_SUBMISSIONS:
    contest, password, username, points = command.split('=>')

    # Check if the contest and password are valid
    if contest in contest_passwords.keys() and contest_passwords[contest] == password:
        # Check if the user already has points for this contest
        if username in user_points.keys():
            # Check if the user's new points are higher than their existing points for this contest
            if contest in user_points[username].keys():
                if user_points[username][contest] < int(points):
                    user_points[username][contest] = int(points)
            else:
                user_points[username][contest] = int(points)
        else:
            user_points[username] = {contest: int(points)}

    command = input()

# Define a helper function to get the total points of a user
def get_total_points(user):
    return sum(user[1].values())

# Find the user with the highest total points
user_list = list(user_points.items())
best_user = max(user_list, key=get_total_points)

#best_user = max(user_points.items(), key=lambda x: sum(x[1].values())) # alternative solution to the one above

# Print the best user and their total points
print(f"Best candidate is {best_user[0]} with total {sum(best_user[1].values())} points.")

# Print a ranking of all users and their points for each contest
print("Ranking:")
for user in sorted(user_points.keys()):
    print(user)
    for contest, points in sorted(user_points[user].items(), key=lambda x: (-x[1], x[0])):
        print(f"#  {contest} -> {points}")
