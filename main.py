from correction import qr_code_binary_capacities as version_data
from codeword import qr_code_data_codeword_capacities as codeword_capacity
from polynomial import binary_to_polynomial

# Define the text
text = str(input("Enter Text: "))

# Convert each character to its ASCII value
def ascii_converter(text):              #Defines a new function for ascii converter 
    ascii_values = [ord(char) for char in text]
    return ascii_values

# Print the ASCII values
ascii_values = ascii_converter(text)

# Convert the decimal into binary 
def decimal_to_binary(decimal_list):
    binary_list = [format(num, '08b') for num in decimal_list]
    return binary_list

binary_nums = decimal_to_binary(ascii_values)

# selecting the version required
def version(total_char):
    char_capacity = len(total_char)
    model = version_data['H']
    # print(model)
    for key, value in model.items():
        if char_capacity <= value:
            return key

# Analyzing the grid size
def grid_size(version_no):
    size = 21 + 4*(version_no - 1)
    return size

version_number = version(binary_nums)


grid = grid_size(version_number)



# ----------------------------------------------------------------------------------------------------------------------------------------
# STRUCTURAL ENCODING DATA 

# Codeword Capacity of given version number
capacity = codeword_capacity["H"][version_number]

# Define which mode of data is being input in the QR code
mode = "0100"   #Byte Mode

# Define character count 
char_count = format(len(binary_nums), '08b')

# Define the Terminator
def terminator():  
    total_char = len(binary_nums)*8
    difference = int(capacity)-int(total_char)
    if difference<4:
        terminator = "0"*(difference)
    else:
        terminator = "0000"
    return terminator

term = terminator()

# Define the final length of data bits after terminator
term_len = int(len(mode))+int(len(char_count))+int(len(binary_nums)*8)+int(len(term))

# Define Number of 0s added to make the length multiple of 8
def multiples():
    num = term_len%8
    if num== 0:
        return 
    else:
        return "0"*num

num_needed = multiples()

# Define number of padding bytes
def pad():
    local_len = term_len
    if num_needed is not None:
        local_len += int(len(num_needed)) 
    difference = int(capacity) - local_len

    pad1 = "11101100"  #Binary for 236 (0xEC)
    pad2 = "00010001"  #Binary for 17  (0x11)

    pad_bytes = []

    for i in range(difference//8):
        alt = i%2
        if(alt == 0):
            pad_bytes.append(pad1)
        else:
            pad_bytes.append(pad2)

    return pad_bytes

pad_bytes = pad()

# Final string after regrouping everything
final_string = mode + char_count + ("".join(binary_nums)) + term + ("".join(pad_bytes))

# Regrouping final string into blocks of 8 bit each
def regroup_final_string(s, block_size=8): 
    return [s[i:i + block_size] for i in range(0, len(s), block_size)]

# Final list of Bytes
final_bytes = regroup_final_string(final_string)
print(final_bytes)

#  Final list of polynomials
polynomial_list = binary_to_polynomial(final_bytes)
print(polynomial_list)
