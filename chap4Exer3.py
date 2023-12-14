#Exercise 3: Reading to a List ☑️
#The file numbers.txt has a list of 100 integer numbers each
#on a newline. Create a python program that puts this data into a list,
#then output the values in integer format.

#Specifying the files containing numbers
file_path = "numbers.txt"

try:
    #Trying to open the file for reading
    with open(file_path, 'r') as file:
        #Reading each line from the file, converting it into integer and storing it in a list
        numbers = [int(line.strip()) for line in file]

    #Printing the values in integer format
    print("Values in integer format:")
    for number in numbers:
        print(number)

#Handling the case where file is not found
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")

#Handling the case where a line in the file cannot be converted to an integer
except ValueError:
    print(f"Error: Unable to convert a line in '{file_path}' to an integer.")

#Handling the other unexpected errors
except Exception as e:
    print(f"An unexpected error occurred: {e}")
