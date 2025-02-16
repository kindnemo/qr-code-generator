#  A function that converts the binary list to polynomials
def binary_to_polynomial(binary_list):
    polynomials = []
    for binary in binary_list:
        terms = []
        degree = len(binary) - 1
        for i, bit in enumerate(binary):
            if bit == '1':
                if degree - i == 0:
                    terms.append("1")   # if constant term than 1
                elif degree - 1 == 1:
                    terms.append("x")   # if x^1 then just x
                else:
                    terms.append(f"x^{degree-i}") # for higher degree terms
        polynomials.append(" + ".join(terms) if terms else "0") # joins terms or return "0"
    return polynomials


# Lookup function that tallies the polynomial with the respective value in the log / anti-log table and returns the a^n representation of the polynomial 

def polynomial_to_exponent(binary_num, table):
    # Converting the binary num to decimal fro tallying
    decimal_number = 0
    for digit in binary_num:
        decimal_number = decimal_number * 2 + int(digit)

    # Looking up the said decimal number in the table
    return(table.get(decimal_number))

