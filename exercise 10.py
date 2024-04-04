def extract_digits_reverse(number):
   
    num_str = str(number)[::-1]
   
    for digit in num_str:
        print(digit)

#Testing
number = 123456
print("Digits extracted in reverse order:")
extract_digits_reverse(number)
