#taking user's input
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

#creating product variable
product = num1*num2

#applying condition and displaying results
if product <= 1000:
    print (product)
else:
    print (num1 + num2)
