# Write a python file that will read the text file and generate a dictionary from the data in the file. The numbers will be the keys and the strings of letters will be the values for the dictionary.

dictionary = {}

with open("raw_dict.txt", "r") as file:
    for line in file:
        parts = line.strip().split(' ')
        if len(parts) == 2:
            key = int(parts[0])
            value = parts[1]
            dictionary[key] = value


print(dictionary)
