import sqlite3

field_mapping = {
    '1': 'name',
    '2': 'street_address',
    '3': 'city',
    '4': 'state',
    '5': 'postal_code',
    '6': 'phone',
    '7': 'email'
}

# factory to handle data transmission 
class DatabaseConnector:
    def __init__(self):
        self.connection = sqlite3.connect('dp_customers.db')
        self.cursor = self.connection.cursor()

    def read_customers(self):
        self.cursor.execute("SELECT * FROM Customers")
        rows = self.cursor.fetchall()
        return rows
    
    def search_customers(self, search):
        try:
            customer_id = int(search)
        except ValueError:
            print("Invalid customer ID. Please enter a valid integer.")
            return []
        
        query = """SELECT customer_id, name, street_address, city, state, postal_code, phone, email 
                FROM Customers 
                WHERE customer_id = ?"""
        self.cursor.execute(query, (customer_id,))
        rows = self.cursor.fetchall()
        return rows

    
    def update_customers(self, customer_id, field, new_value):
        if field not in ['name', 'city', 'state', 'postal_code', 'phone', 'email', 'street_address']:
            print("Invalid field. Update not performed.")
            return
        
        update_query = f"UPDATE Customers SET {field} = ? WHERE customer_id = ?"
        self.cursor.execute(update_query, (new_value, customer_id))
        self.connection.commit()
        print(f"Customer {field} updated to {new_value}.")

        
    def add_customers(self, add_values):
        add_query = """
        INSERT INTO Customers (name, street_address, city, state, postal_code, phone, email)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        self.cursor.execute(add_query, add_values)
        self.connection.commit()
        print("New customer has been added.")
        
    def delete_customers(self, customer_id):
        delete_query = "DELETE FROM Customers WHERE customer_id = ?"
        self.cursor.execute(delete_query, (customer_id,))
        self.connection.commit()

def display_customer_info(customers):
    print("--- Customers ---")
    print(f'{"ID":<12} {"Name":<12} {"City":<28} {"Phone":<23} {"Email":<23}')
    for row in customers:
        if row is not None and all(field is not None and field != "" for field in row):
            print(f'{row[0]:<10} {row[1]:<25} {row[3]:<25} {row[6]:<25} {row[7]:<25} ')

def display_one_customer(customer):
    if customer:
        print("+++ Customer Detail +++")
        print(f'{"ID:":<15}{customer[0]}\n{"Name:":<15}{customer[1]}\n{"Address:":<15} {customer[2]}\n{"City:":<15}{customer[3]}\n{"State:":<15}{customer[4]}\n{"Zip Code:":<15}{customer[5]}\n{"Phone:":<15}{customer[6]}\n{"Email:":<15}{customer[7]}\n')
    else:
        print("No customer found with that ID.")

def print_update_options():
    for number, field in field_mapping.items():
        print(f"[{number}] {field.capitalize()}")

def main_menu():
    greeting = "****** Customer Database ******"
    print("-" * len(greeting))
    print(greeting)
    print("-" * len(greeting))

    db_connector = DatabaseConnector()

    while True:
        print("Main Menu:")
        print("[1] View All Customers")
        print("[2] Search Customers")
        print("[3] Add a new Customer")
        print("[0] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rows = db_connector.read_customers() 
            print("\nCustomer Information:")
            display_customer_info(rows) 

            while True:
                inner_choice = input("Enter a Customer ID to view a Customer:\nOr press '0' to return to the main menu: ")
                if inner_choice != '0':
                    customer_id = int(inner_choice)
                    rows = db_connector.search_customers(customer_id)
                    if rows:
                        print("\nCustomer Information:")
                        display_one_customer(rows[0])
                    else:
                        print("No customer found with that ID.")
                else:
                    break

        elif choice == "2":
            search = input("Enter the Customer ID: \n")
            rows = db_connector.search_customers(search)
            if rows:
                display_one_customer(rows[0])
                print("[1] Update Customer")
                print("[2] Delete Customer")
                print("[0] Return to Main Menu")
                while True:  
                    field_choice = input("Select an option: ")
                    if field_choice == '1':
                        print_update_options()
                        update_choice = input("Enter the number for the field to update: ")
                        if update_choice in field_mapping:
                            field = field_mapping[update_choice]
                            new_value = input(f"Enter the new {field}: ")
                            db_connector.update_customers(search, field, new_value)
                            print(f"{field.capitalize()} updated successfully.")
                        else:
                            print("Invalid field selection. Please try again.")
                    elif field_choice == '2':
                        confirm_delete = input("Are you sure you want to delete this customer? Type 'y' to confirm or 'n' to cancel: ").lower()
                        if confirm_delete == 'y':
                            db_connector.delete_customers(search)
                            print("Customer deleted.")
                            break 
                        else:
                            print("Customer deletion canceled.")
                    elif field_choice == '0':
                        print("Returning to the main menu...")
                        break
                    else:
                        print("Invalid command. Please try again.")
            else:
                print("No customer found with that ID.")


        elif choice == "3":
            new_name = input("Enter the new name: ")
            new_address = input("Enter the new street address: ")
            new_city = input("Enter the new city: ")
            new_state = input("Enter the new state: ")
            new_postal_code = input("Enter the new zip code: ")
            new_phone = input("Enter the new phone: ")
            new_email = input("Enter the new email: ")
            
            add_values = (new_name, new_address, new_city, new_state, new_postal_code, new_phone, new_email)
            db_connector.add_customers(add_values)
            print(f"Customer {new_name} successfully added!")

        elif choice == "0":
            print("Exiting the program. Goodbye!")
            db_connector.connection.close()
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 0.")

if __name__ == "__main__":
    main_menu()

