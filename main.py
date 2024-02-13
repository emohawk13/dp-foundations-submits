# Int
print('Converting Int\'s')
num_choice = input("Please select 1 or 0: ")
num = int(num_choice) # Convert String to Int
int_float = float(num)
str_num = str(num)
boo_num = bool(num)

print(f'num: {num} (type: {type(num)})')
print(f'int_float: {int_float} (type: {type(int_float)})')
print(f'str_num: {str_num} (type: {type(str_num)})')
print(f'boo_num: {boo_num} (type: {type(boo_num)})')
print()

# Float
print('Converting Floats')
float_number_choice = input("Please choose a number that has a decimal point (example: '0.75'): ")
float_number = float(float_number_choice)
int_float = int(float_number)
str_float = str(float_number)
boo_float = float_number != 0

print(f'num: {float_number} (type: {type(float_number)})')
print(f'int_float: {int_float} (type: {type(int_float)})')
print(f'str_float: {str_float} (type: {type(str_float)})')
print(f'boo_float: {boo_float} (type: {type(boo_float)})')
print()