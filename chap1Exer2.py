#Exercise 2: Maths ☑️
#Write a program that evaluates the following calculations for two int numbers obtained
#from the user and outputs the results to the console:
#Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)

#Asking user any two integers
num1= int(input("Enter first integer of your choice:"))
num2= int(input("Enter second integer of your choice:"))

#Performing calculation
sum_result= num1 + num2
diff_result= num1 - num2
product_result= num1 + num2

#Checking if the second number is not zero before performing the functions
if num2 !=0:
    quotient_result = num1 / num2
    remainder_result = num1 % num2
else:
     quotient_result = "Undefined (division by zero)"
     remainder_result = "undefined (division by zero)"

#Output
print(f"Sum: {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")
print(f"Remainder: {remainder_result}")
