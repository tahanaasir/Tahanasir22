#Exercise C: Calculator Function☑️
#The program should display the following calculator menu:

#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Modulus
#The program will prompt the user to choose the operation choice (from 1 to 5).
#Then it asks the user to input values for the calculation. The program outputs the
#results of the calculation. The program should end by asking if the user would like to
#perform another calculation or not.

#Defining functions for each operation
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    #Checking for division by zero
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


def modulus(x, y):
    #Checking for modulus by zero
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero"


#Main loop for the calculator
while True:
    #Displaying the calculator menu
    print("\nCalculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    #Asking user to enter there choice number
    choice = input("Enter your choice (1-5): ")

    #Checking if the choice is valid
    if choice.isdigit() and 1 <= int(choice) <= 5:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        #Performing the chosen operation
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

        #Displaying the result
        print("Result:", result)

        #Asking if the user wants to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()

        #Exiting the loop if the user does not want to perform another calculation
        if another_calculation != 'yes':
            break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
