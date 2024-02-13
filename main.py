# Leap Year Finder

def player_input():
    while True:
        try:
            user_input = int(input("Enter a year: "))
            if user_input >= 1752:
                return user_input
            else:
                print("Please use a year after 1752 AD.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def game_start():
    print("Welcome to Leap Year Finder")
    while True:
        year = player_input()
        result = is_leap_year(year)
        print(result)
        
        continue_input = input("Would you like to continue? (yes/no): ").strip().lower()
        if continue_input not in ["yes", "y", ""]:
            break

game_start()
