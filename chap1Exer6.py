#Exercise 6: FizzBuzz ☑️
#Write a program that prints the numbers from 1 to 100. But for
#multiples of three print Fizz” instead of the number and for the multiples
#of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

#Iterate numbers from 1 to 100
for num in range (1, 101):
    #Check if the numbers is a multiple of both 3 and 5
    if num % 3 == 0 and num % 5 ==0:
        print("FizzBuzz")
    #Check if the number is multiple of 3
    elif num % 3 == 0:
        print("Fizz")
    #Check if the number is multiple of 5
    elif num % 5 == 0:
        print("Buzz")
    #If the number is not multiple of both 3 and 5 then print the number by itself
    else:
        print(num)
