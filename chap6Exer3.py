#Exercise 3: Calculator☑️
#Write a program that will display the following calculator menu

#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Modulus
#6. Check greater number
#The program will prompt the user to choose the operation choice (from 1 to 6).
#Then it asks the user to input values for the calculation.
#The program outputs the results of the calculation.Use operator module functions

#Extension Problem (Bonus):
#Allow the user to keep entering values until they enter Q to quit.
#Handle incorrect input

import operator

#Function to perform addition
def add(x, y):
    return operator.add(x, y)

#Function to perform subtraction
def subtract(x, y):
    return operator.sub(x, y)

#Function to perform multiplication
def multiply(x, y):
    return operator.mul(x, y)

#Function to perform division
def divide(x, y):
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Cannot divide by zero"

#Function to perform modulus
def modulus(x, y):
    return operator.mod(x, y)

#Function to check which number is greater
def check_greater(x, y):
    return operator.gt(x, y)

#Main program loop
while True:
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Q. Quit")

    #Getting user input for choice
    choice = input("Enter your choice (1-6, or Q to quit): ").upper()

    #Checking if the user wants to quit
    if choice == 'Q':
        print("Exiting the calculator. Goodbye!")
        break

    #Validate user choice
    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please enter a number between 1 and 6, or Q to quit.")
        continue

    try:
        #Getting user input for numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    #Performing the selected operation based on user choice
    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = modulus(num1, num2)
    elif choice == '6':
        result = check_greater(num1, num2)
        print(f"{num1} is greater than {num2}: {result}")
        continue

    #Displaying the result of the calculation
    print(f"Result: {result}")
