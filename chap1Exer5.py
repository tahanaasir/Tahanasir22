#Exercise 5: Continue ☑️
#Write a program that implements a while loop.
#This program should ask the user if they would like
#to continue and use the while loop to keep looping as long
#as they enter the letter Y. Once the while loop has terminated output
#the number of times it is executed.

# Initialize a counter for the number of loop iterations
count= 0

#Asking user if they want to continue looping
while True:
    user_input= input("Do you want to continue the loop? (Y/N): ").upper()

    # Increment the counter for each iteration
    count += 1

    #Checking if the user wants to continue or no
    if user_input !='Y':
        break

#Counting how many times the loop is executed
print(f"The loop was executed {count} times. ")
