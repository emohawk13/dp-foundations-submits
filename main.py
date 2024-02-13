# Hogwarts Sorting Hat Program

# Initialize the point counters for each house
gryffindor_count = 0
ravenclaw_count = 0
hufflepuff_count = 0
slytherin_count = 0

# Define questions then the corresponding answers
questions = [
    "What trait do you value most in yourself and others?\nA. Bravery\nB. Intelligence\nC. Kindness\nD. Ambition\n",
    "You're faced with a difficult decision. What's your typical approach?\nA. Act quickly, without hesitation.\nB. Analyze the situation thoroughly and make an informed choice.\nC. Consider how your decision will impact others and choose accordingly.\nD. Take the path that will lead to the greatest overall success.\n",
    "Which of the following animals would you choose as a pet?\nA. Lion\nB. Owl\nC. Badger\nD. Snake\n",
    "You've been given a puzzle to solve. How do you approach it?\nA. Dive in headfirst and try different solutions until one works.\nB. Study the puzzle carefully, break it down into smaller parts, and solve it methodically.\nC. Collaborate with others to brainstorm solutions.\nD. Use your creativity and think outside the box to find a unique solution.\n",
    "Which of these magical objects would you most want to possess?\nA. Sword of Gryffindor\nB. Invisibility Cloak\nC. Resurrection Stone\nD. Locket of Slytherin\n"
]

# Iterate through questions and get user answers
for i, question in enumerate(questions, start=1):
    answer = input(f"Question {i}:\n{question}").strip().lower()
    if answer == 'a':
        gryffindor_count += 1
    elif answer == 'b':
        ravenclaw_count += 1
    elif answer == 'c':
        hufflepuff_count += 1
    elif answer == 'd':
        slytherin_count += 1
    else:
        print("Invalid input. Please choose A, B, C, or D.")

# Determine the house with the most points
house_points = {
    "Gryffindor": gryffindor_count,
    "Ravenclaw": ravenclaw_count,
    "Hufflepuff": hufflepuff_count,
    "Slytherin": slytherin_count
}

# Find the house with the highest count
sorted_houses = sorted(house_points.items(), key=lambda x: x[1], reverse=True)
winner_house, winner_points = sorted_houses[0]

# Define traits for each house
traits = {
    "Gryffindor": "Daring, bravery, and chivalry.",
    "Hufflepuff": "Patience, loyalty, and hard work.",
    "Ravenclaw": "Intelligence, creativity, and wit.",
    "Slytherin": "Cunning, ambition, and a hunger for power."
}

# Display the sorting result and traits
print("\nSorting Hat's Verdict:")
print(f"You belong in {winner_house}, known for {traits[winner_house]}")
