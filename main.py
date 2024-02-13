# Christmas Tree Program

height = int(input("Enter the height of the tree: "))
print("Here is your tree:")

# For loop that takes the user input and builds the star pattern
for i in range(1, height + 1):
    print((" " * (height - i)) + ("* " * i))
top_star_width = 2 * height - 1

trunk_height = int(height / 2)
trunk_width = int(height / 2 + 1)
spaces_before_trunk = int((top_star_width - trunk_width) / 2)

for _ in range(trunk_height):
    print((" " * spaces_before_trunk) + ("*" * trunk_width))

