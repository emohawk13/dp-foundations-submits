import csv
import os

def print_menu():
    print("\n**** Address Book ****")
    print("What would you like to do?")
    print(" (A)dd a name")
    print(" (R)emove a name")
    print(" (F)ind a name")
    print(" (Q)uit")

def print_address_book(list_of_dicts, search="", with_indexes=False):
    leader_title = ""
    leader_lines = ""
    if with_indexes:
        leader_title = "Index "
        leader_lines = "------"
    print(
        f'{leader_title} {"First Name":^10} {"Last Name":^15} {"Address":^20} {"City":^15} {"State":^6}'
    )
    print(f'{leader_lines} {"-"*10} {"-"*15} {"-"*20} {"-"*15} {"-"*6}')

    for index, row in enumerate(list_of_dicts):
        num_string = ""
        if with_indexes:
            num_string = f"{index:6}. "

        matches_search = True
        if search:
            if not (
                search in row["First Name"]
                or search in row["Last Name"] 
                or search in row["Address"]
                or search in row["City"]
                or search in row["State"]
            ):
                matches_search = False
                print_address_book(address_book)
                print("Contact not found please try again")
        if matches_search:
            print(
                f'{num_string} {row["First Name"]:10} {row["Last Name"]:15} {row["Address"]:20} {row["City"]:15} {row["State"]:^6}'
            )

def find_user():
    return input("Enter a search term: ")

def add_user(address_book):
    print("Add a new User:")
    new_user = {}
    new_user["First Name"] = input(" First Name: ")
    new_user["Last Name"] = input("  Last Name: ")
    new_user["Address"] = input("    Address: ")
    new_user["City"] = input("       City: ")
    new_user["State"] = input("      State: ")

    try:
        address_book.append(new_user)
    except ValueError:
        print("Something went wrong, please try again")

def remove_user(address_book):
    print_address_book(address_book, with_indexes=True)
    try:
        user_input = int(input("Which user would you like to remove? (Enter number) "))
        if 0 <= user_input < len(address_book):
            removed_user = address_book.pop(user_input)
            print(
                f"User '{removed_user['First Name']} {removed_user['Last Name']}' removed!\n"
            )
            save_address_book(address_book)
        else:
            print("Invalid user index. Please enter a valid index.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def save_address_book(address_book):
    try:
        with open("address_book.csv", "w", newline="") as csvout:
            csvwriter = csv.DictWriter(csvout, fieldnames=address_book[0].keys())
            csvwriter.writeheader()
            csvwriter.writerows(address_book)

    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def load_address_book():
    address_book = []
    file_path = "address_book.csv"

    if not os.path.exists(file_path):
        return address_book

    with open(file_path, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            address_book.append(row)

    return address_book

search_term = ""

while True:
    address_book = load_address_book()
    print_address_book(address_book, search=search_term)
    search_term = ""
    print_menu()
    user_input_menu = input().upper()

    if user_input_menu == "A":
        add_user(address_book)
        print("New user added!\n")
        save_address_book(address_book)
    elif user_input_menu == "R":
        remove_user(address_book)
        print("User removed! \n")
        save_address_book(address_book)
    elif user_input_menu == "F":
        search_term = find_user()
    elif user_input_menu == "Q":
        break
