#Exercise A: Multiplication Tables ☑️
#Write a program to print Multiplication table in
#following format from 1 to 10 tables Hint: Use nested loops

#Multiplication table of : 1
#1 x 1 = 1
#1 x 2 = 2
#1 x 3 = 3
#1 x 4 = 4
#1 x 5 = 5
#1 x 6 = 6
#1 x 7 = 7
#1 x 8 = 8
#1 x 9 = 9
#1 x 10 = 10
#…
#Multiplication table of : 10
#10 x 1 = 10
#10 x 2 = 20
#10 x 3 = 30
#10 x 4 = 40
#10 x 5 = 50
#10 x 6 = 60
#10 x 7 = 70
#10 x 8 = 80
#10 x 9 = 90
#10 x 10 = 100

#Multiplication table from 1 to 10
for i in range(1, 11):  # Outer loop for the table number
    print(f"\nMultiplication table of : {i}")

    #Inner loop for multiplication within the table
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
