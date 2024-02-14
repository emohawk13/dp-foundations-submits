# Binary to Decimal
def binary_to_decimal(binary_str):
    if isinstance(binary_str, str) and len(binary_str) == 8:
        if all(bit in '01' for bit in binary_str):
            decimal = int(binary_str, 2)
            if 0 <= decimal <= 255:
                return decimal
    raise ValueError("Input must be an 8-character binary string (0s and 1s) representing a number in the range [0, 255].")

while True:
    user_input = input("Enter an 8-character binary number: ")
    try:
        decimal_number = binary_to_decimal(user_input)
        print(decimal_number)
        break
    except ValueError:
        print("Invalid input. Please enter a valid 8-character binary number.")
