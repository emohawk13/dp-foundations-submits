# Number guessing game
import random

def numbergen():
    return random.randint(1, 100)

def player_input():
    while True:
        try:
            user_input = int(input("Please choose a number from 1 to 100: "))
            return user_input
        except ValueError: 
            print("Please use a number.")

def game_start():
    target_number = numbergen()
    print("Welcome to the number guessing game!")
    guess_count = 0
    
    while True:
        guess = player_input()
        guess_count += 1
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {guess_count} guesses.")
            break
        
        if guess_count % 2 == 0 and guess_count != 2:
            print(f"You've made {guess_count} guesses. Keep going!")
        elif guess_count % 3 == 0 and guess_count != 2:
            print(f"You've made {guess_count} guesses. Can you guess it?")
        elif guess_count % 4 == 0 and guess_count != 2:
            print(f"You've made {guess_count} guesses. You're getting closer!")
        if guess_count % 5 == 0:
            reveal_option = input(f"You've made {guess_count} attempts. Do you want to reveal the target number? (Type '0' to reveal and quit, or press Enter to continue): ")
            if reveal_option == '0':
                print(f"The target number was {target_number}. Thanks for playing!")
                break

game_start()


