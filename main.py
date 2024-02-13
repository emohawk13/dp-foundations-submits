# Initialize a dictionary to store team data
teams = {}

while True:
    # Print the Key-Value pairs separated by a space
    for key, value in teams.items():
        print(f"{key} {value}")

    # Ask the user what to do next
    choice = (
        input(
            "What would you like to do next?\n"
            "a. (A)dd a new team\n"
            "b. (R)emove a team\n"
            "c. (S)how\n"
            "d. (Q)uit\n"
            "Enter your choice: "
        )
        .strip()
        .lower()
    )

    if choice == "q":  # If the user enters Q, the program ends
        break

    elif choice == "s":  # If the user enters S, show the entire dictionary
        if not teams:
            print("The dictionary is empty.")
        else:
            print(teams)

    elif choice == "r":  # If the user enters R, remove a team
        key_to_remove = input("Enter the key of the team to remove: ").strip()
        if key_to_remove in teams:
            del teams[key_to_remove]
            print(f"Team '{key_to_remove}' has been removed.")
        else:
            print(f"Team '{key_to_remove}' not found.")

    elif choice == "a":  # If the user enters A, add a new team
        team_location = input("Enter the location of the team: ").strip()
        team_mascot = input("Enter the mascot of the team: ").strip()
        if team_location and team_mascot:
            teams[team_location] = team_mascot
            print(f"Team '{team_location}' with mascot '{team_mascot}' has been added.")
        else:
            print("Both location and mascot must be provided.")
    else:
        print("Invalid choice. Please choose A, R, S, or Q.")
