#Exercise 13: Product of list items☑️
#Write a program that passes a list as an argument to a function. The function should then calculate the product
#(values multiplied) of the list values and return this value back to the main program.

#Functions to calculate the values in a list

def calculate_the_product(input_list):
    product= 1
    for value in input_list:
        product *= value
        return product

#Example
numbers = [1, 2, 3, 4, 5]

#Calling the function from the example list
result= calculate_the_product(numbers)

#Result
print("The product of the list is: ", result)
