def print_numbers_divisible_by_5(numbers):
    for num in numbers:
        if num % 5 == 0:
            print(num)

# Testing
numbers = [10, 15, 12, 25, 30, 18, 40]

print("Numbers divisible by 5:")
print_numbers_divisible_by_5(numbers)
