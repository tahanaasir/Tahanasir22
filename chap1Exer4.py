#Exercise 4: Largest Number ☑️
#Write a program to input three numbers and outputs the largest using the multiple if -else statements

#Asking user for any three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

#Comparing all the three number to find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
else:
     if num2 >= num1 and num2 >= num3:
         largest = num2
     else:
          largest = num3

#Result
print(f"The largest number is: {largest}")
