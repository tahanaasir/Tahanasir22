#Exercise 7: Even Numbers ☑️
#Write a program that prints the even numbers from 1 to 100. Hint - Use Continue Statement.

#Iterate numbers from 1 to 100
for num in range(1, 101):
    #Check if the number is odd, then skip to the next illeteration
    if num % 2 !=0:
        continue
    #Only print if the number is even
    print(num)
