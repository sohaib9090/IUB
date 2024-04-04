def is_palindrome(num):
   
    num_str = str(num)
   
    return num_str == num_str[::-1]

# Testing
num1 = 121
num2 = 123123

print(num1, "is palindrome?", is_palindrome(num1))
print(num2, "is palindrome?", is_palindrome(num2)) 
