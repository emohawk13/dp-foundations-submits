# Create a program that will run a movie theater

# Requirements:
#   1. Different prices for kids under 3, under 12 (kids ticket), adults (12-65), and seniors (65+) -Done
#   2. 3-5 different Movies with 4-5 showtimes each - Done
#   3. Ability to buy multiple tickets - Done
#   4. Concessions which include Popcorn, Drink, Hotdog, Nachos, Candy with prices - should be able to choose more than one - Done
#   5. Checkout with subtotal and tax - Done

# Movie data List
movies = [
    {"title": "This Movie", "showtimes": ["10:00 AM", "2:00 PM", "6:00 PM", "9:00 PM"]},
    {"title": "That Movie", "showtimes": ["11:00 AM", "3:00 PM", "7:00 PM", "9:00 PM"]},
    {"title": "DJ Khaled presents Another One", "showtimes": ["11:00 AM", "3:00 PM", "7:00 PM", "9:00 PM"]},
    {"title": "DJ Khaled presents Another One part 2", "showtimes": ["11:00 AM", "3:00 PM", "7:00 PM", "9:00 PM"]},
]

# Ticket prices List
ticket_prices = {
    "kid": 5.0,
    "child": 10.0,
    "adult": 15.0,
    "senior": 12.0
}

# Concession prices List
concession_prices = {
    "popcorn": 5.0,
    "drink": 3.0,
    "hotdog": 4.0,
    "nachos": 4.5,
    "candy": 2.5
}

def select_movie():
    print("Select a movie:")
    for i, movie in enumerate(movies):
        print(f"{i + 1}. {movie['title']}")
    choice = int(input("Enter the number for the movie: ")) - 1
    return movies[choice]

def select_showtime(movie):
    print(f"Select a showtime for {movie['title']}:")
    for i, showtime in enumerate(movie['showtimes']):
        print(f"{i + 1}. {showtime}")
    choice = int(input(f"Select the number to choose showtime for {movie['title']}: ")) - 1
    return movie['showtimes'][choice]

def buy_tickets():
    num_tickets = int(input("Enter the number of tickets: "))
    subtotal = 0.0
    for _ in range(num_tickets):
        print("Select a ticket type:")
        print("1. Kid (Under 3)")
        print("2. Child (3-12 years)")
        print("3. Adult (12-65 years)")
        print("4. Senior (65+ years)")
        ticket_type = int(input("Enter the number of the ticket type: "))
        if ticket_type == 1:
            subtotal += ticket_prices["kid"]
        elif ticket_type == 2:
            subtotal += ticket_prices["child"]
        elif ticket_type == 3:
            subtotal += ticket_prices["adult"]
        elif ticket_type == 4:
            subtotal += ticket_prices["senior"]
    return subtotal

def order_concessions():
    total_cost = 0.0
    while True:
        print("Select a concession item:")
        for i, item in enumerate(concession_prices.keys()):
            print(f"{i + 1}. {item} (${concession_prices[item]})")
        print("0. Done ordering")
        choice = int(input("Enter the number of the item (or 0 to finish): "))
        if choice == 0:
            break
        elif choice - 1 in range(len(concession_prices)):
            item = list(concession_prices.keys())[choice - 1]
            quantity = int(input(f"Enter the quantity of {item}: "))
            total_cost += concession_prices[item] * quantity
    return total_cost

def calculate_total(subtotal, concessions_cost):
    tax_rate = 0.08
    tax = (subtotal + concessions_cost) * tax_rate
    total = subtotal + concessions_cost + tax
    return total

def movie():
    print("Welcome to the Movie Theater!")
    
    selected_movie = select_movie()
    selected_showtime = select_showtime(selected_movie)
    subtotal = buy_tickets()
    concessions_cost = order_concessions()
    total = calculate_total(subtotal, concessions_cost)

    # 4 receipt
    print("\nReceipt:")
    print(f"Movie: {selected_movie['title']} ({selected_showtime})")
    print(f"Ticket Subtotal: ${subtotal:.2f}")
    print(f"Concessions Total: ${concessions_cost:.2f}")
    print(f"SubTotal: ${subtotal + concessions_cost:.2f}")
    print(f"Tax: ${total - subtotal - concessions_cost:.2f}")
    print(f"Total: ${total:.2f}")
    print("Enjoy the movie!")

if __name__ == "__main__":
    movie()
