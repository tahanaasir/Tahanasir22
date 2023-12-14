#Exercise 3: Is it Triangle ☑️
#Write a program that asks the user to enter the lengths of the
#three sides of a triangle. Use the triangle inequality to determine
#if we have a triangle: In mathematics, the triangle inequality states that
#for any triangle, the sum of the lengths of any two sides must be greater than
#or equal to the length of the remaining side

#Asking the user to enter the lenths
side1= float(input("Enter the lenght of the first side: "))
side2= float(input("Enter the lenght of the second side: "))
side3= float(input("Enter the lenght of the third side: "))

#Cheking the triangle inequality
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("These sides lenghts form a valid triangle. ")
else:
     print("These sides lenghts do not a valid triangle. ")
