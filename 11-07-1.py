# Define a list of types
"""types = ['int', 'float', 'str', 'bool', 'list']

# Define a conversion matrix
# 'Yes' - conversion possible
# 'No'  - conversion not directly possible
# 'If numeric' or 'If formatted' - possible with condition
conversion_table = {
    'int':    ['Yes', 'Yes', 'Yes', 'Yes', 'No'],
    'float':  ['Yes', 'Yes', 'Yes', 'Yes', 'No'],
    'str':    ['If numeric', 'If numeric', 'Yes', 'Yes', 'If formatted'],
    'bool':   ['Yes', 'Yes', 'Yes', 'Yes', 'No'],
    'list':   ['No', 'No', 'Yes', 'Yes', 'Yes']
}

# Print the header
print(f"{'From \\ To':<10}", end="")
for to_type in types:
    print(f"{to_type:^12}", end="")
print()

# Print each row of the table
for from_type in types:
    print(f"{from_type:<10}", end="")
    for result in conversion_table[from_type]:
        print(f"{result:^12}", end="")
    print()"""

#convert an integer to binary
num = 10
binary = bin(num)
print(binary)  # Output: 0b1010
#Convert Binary to Integer
binary_str = '1010'
decimal = int(binary_str, 2)
print(decimal)  # Output: 10
