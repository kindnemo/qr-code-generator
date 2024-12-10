# Define the text
text = str(input("Enter Text: "))

# Convert each character to its ASCII value
ascii_values = [ord(char) for char in text]

# Print the ASCII values
print(ascii_values)


# Convert the decimal into binary 
def decimal_to_binary(decimal_list):
    binary_list = [format(num, '08b') for num in ascii_values]
    return binary_list


binary_nums = decimal_to_binary(ascii_values)
print(binary_nums)


# selecting the version required
def version(total_char):
    char_capacity = len(total_char)*8
    model = version_data['H']
    # print(model)
    for key, value in model.items():
        if char_capacity <= value:
            return key


version_number = version(binary_nums)
print(version_number)


# Analyzing the grid size
def grid_size(version_no):
    size = 21 + 4*(version_no - 1)
    return size


grid = grid_size(version_number)
print(grid)
