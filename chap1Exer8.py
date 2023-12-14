#Exercise 8: Print Pattern ☑️
#Write a program to display the following pattern using nested loops.

#Defining the number of rows for the pattern
rows= 5

#Outer loop for the number of rows
for i in range(1, rows + 1):
    #Inner loop for each row to print numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    #Move to the next line after each row
    print()