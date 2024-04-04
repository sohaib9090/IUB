def remove_chars(input_string, n):
    return input_string[n:]

# Ask the user for input
input_string = input("Enter a string: ")
n = int(input("Enter the number of characters to remove: "))

# Display the modified string
print("Modified string:", remove_chars(input_string, n))
