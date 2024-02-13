# Calendar App
days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
months = [
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December",
]

def user_input():
    global year, start_day, num_days, month_choice 
    while True:
        try:
            day_of_week = input(
                f"Please choose from this list which day does the chosen month start on: \n {', '.join(days_of_week)}: "
            )
            if day_of_week in days_of_week:
                start_day = day_of_week
                break
            else:
                print("Please select a day from the provided list.")
        except ValueError:
            print("Please use the provided list.")
    while True:
        try:
            month_choice = input(
                f"Please choose from this list which month you'd like: \n {', '.join(months)}: "
            )
            if month_choice in months:
                break
            else:
                print("Please select a month from the provided list.")
        except ValueError:
            print("Please use the provided list.")
    while True:
        try:
            year = int(input("Please enter the year you would like to use: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    while True:
        try:
            num_days = int(input("Please enter the number of days for your month: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def generate_calendar(year, month_choice, start_day, num_days):
    start_index = days_of_week.index(start_day)
    print(f"{month_choice} {year}\n")
    print("  ".join(days_of_week))
    leading_spaces = ["  "] * start_index
    calendar_rows = [[]] 
    day = 1
    calendar_rows[-1].extend(leading_spaces)

    while day <= num_days:
        calendar_rows[-1].append(f"{day:2d}")
        day += 1

        if len(calendar_rows[-1]) == 7:
            calendar_rows.append([])  
    while len(calendar_rows[-1]) < 7:
        calendar_rows[-1].append("")
    for row in calendar_rows:
        print("   ".join(row))

def start_calendar_app():
    user_input()
    generate_calendar(year, month_choice, start_day, num_days)

if __name__ == "__main__":
    start_calendar_app()


