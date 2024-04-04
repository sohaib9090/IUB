previous_number = 0
current_number = 0

for i in range(10):
    # Calculating the sum of the numbers
    current_number = i
    sum_of_numbers = previous_number + current_number
    # Print the sum
    print("Sum of", current_number, "and", previous_number, "is:", sum_of_numbers)
    # Update variables for the next iteration
    previous_number = current_number