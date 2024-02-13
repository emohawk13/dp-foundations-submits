# Calendar App
days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
max_days_in_month = {
    "January": 31,
    "February": 28, 
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

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

def user_input(max_days_in_month):
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
            print("Please choose a month:")
            for i, month in enumerate(max_days_in_month.keys(), start=1):
                print(f"{i}. {month}")
            month_choice_num = int(input("Enter the number for the month: "))
            months_list = list(max_days_in_month.keys())
            if 1 <= month_choice_num <= len(max_days_in_month):
                month_choice = months_list[month_choice_num - 1]
                break
            else:
                print("Invalid choice. Please select a valid month number.")
        except ValueError:
            print("Invalid input. Please enter a valid month number.")
    
    while True:
        try:
            year = int(input("Please enter the year you would like to use: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    
    if month_choice == "February" and is_leap_year(year):
        num_days = 29
    else:
        num_days = max_days_in_month[month_choice]

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
    user_input(max_days_in_month)
    print("\n")
    generate_calendar(year, month_choice, start_day, num_days)

if __name__ == "__main__":
    start_calendar_app()


