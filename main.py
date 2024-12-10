from correction import qr_code_numeric_capacity

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