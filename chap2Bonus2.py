#Exercise B: Age Calculator
#Create a program to take input of the user('s date of birth and output the age. '
#'Expected input: 8/5/2018 Expected output: Your age is 5 years Hint: you can use the
#'date from datetime package to get today')s date

from datetime import datetime

def calculate_age(birthdate):
    #Getting today's date
    today = datetime.now()

    #Asking user to enter the user's date of birth
    birthdate = datetime.strptime(birthdate, "%m/%d/%Y")

    #Calculating the age
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return age

#Getting user input for date of birth
user_input = input("Enter your date of birth (mm/dd/yyyy): ")

try:
    #Calculating and printing the age
    age = calculate_age(user_input)
    print(f"Your age is {age} years.")
except ValueError:
    print("Invalid date format. Please use mm/dd/yyyy.")
