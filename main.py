# Initialize the dictionary with up to three initial key-value pairs
sports_teams = {
    "Team1": "Location1",
    "Team2": "Location2",
    "Team3": "Location3"
}

# Function to print the key-value pairs
def print_teams(teams):
    for team, location in teams.items():
        print(f"{team} - {location}")

# Main program loop
while True:
    print_teams(sports_teams)
    print("\nWhat would you like to do next?")
    print("(A)dd a new team")
    print("(R)emove a team")
    print("(Q)uit")

    choice = input().strip().upper()

    if choice == "Q":
        break
    elif choice == "R":
        key_to_remove = input("Enter the name of the team to remove: ")
        if key_to_remove in sports_teams:
            del sports_teams[key_to_remove]
            print(f"{key_to_remove} has been removed.")
        else:
            print(f"{key_to_remove} not found in the dictionary.")
    elif choice == "A":
        new_team = input("Enter the name of the new team: ")
        location = input(f"Enter the location of {new_team}: ")
        sports_teams[new_team] = location
        print(f"{new_team} has been added to the dictionary.")
    else:
        print("Invalid choice. Please enter A, R, or Q.")

print("Goodbye!")
