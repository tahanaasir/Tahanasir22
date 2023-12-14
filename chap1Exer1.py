#Exercise 1: User Input Output ☑️
#Write code to prompt the user to input her/his name and age and print
#these details on the screen. Find the length of the name and also the age
#of the user after one year. The format of text should look like the sample output below. (Use title() function)

#Asking user his/her name and age
print("Hello user!")
name= input("What is your name?").title()
age= int(input("What is your age?"))

#Printing user deatils
print(f"It is nice to meet you,{name}")
print("The lenght of your name is: ")
print(len(name))
print(f"You will be {age + 1} in a year.")