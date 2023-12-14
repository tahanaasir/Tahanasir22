#Exercise 12: Area Function☑️
#Code a program to display a menu on the screen that asks if the user wants to
#1: Calculate the area of a square
#2: Calculate the area of a circle
#3: Calculate the area of a triangle
#Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.

import math

#Calculating the area of suqare

def calculate_area_of_square():
    side_length= float(input("Enter the area of sqaure: "))
    area = side_length **2
    print("The area of sqaure is: ", area)

#Calculating the area of circle

def calculate_area_of_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius ** 2
    print("The area of the circle is:", area)

#Calculating the area of triangle

def calculate_area_of_triangle():
    base_length= float(input("Enter the lenght of the base of triangle: "))
    height= float(input("Enter the height of the triangle: "))
    area = 0.5 * base_length * height
    print("The area of triangle is: ", area)

#Displaying menu to get user input
while True:
    print("/nMenu:")
    print("1: Calculate the area of square: ")
    print("2: Calculate the area of circle: ")
    print("3: Calculate the area of triangle: ")
    print("4: To Exit")

    choice = input("Enter the number of your choice (1-4):")

    if choice == 1:
        calculate_area_of_square()
    elif choice == 2:
        calculate_area_of_circle()
    elif choice == 3:
        calculate_area_of_triangle()
    elif choice == 4:
        print("Exiting the program. HAVE A NICE DAY!!!")
        break
    else:
        print("Invalid please the number between 1 to 4")