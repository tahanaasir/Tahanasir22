#Exercise 9: Integer List☑️
#Create an integer list and perform following operations:
#Create an int list with 10 values.
#Output the list using a for loop.
#Output the highest and lowest value.
#Sort the elements in ascending order.
#Sort the elements in descending order.
#Append two elements.
#Print the list after appending.



#Creating an integer list with 10 values
integer_list = [8, 5, 10, 7, 1, 3, 4, 9, 2, 6]

#Printing the lists using a for loop
print("Original list: ")
for num in integer_list:
    print(num, end=" ")
print()

#Printing the highest and lowest value
highest_value= max(integer_list)
lowest_value= min(integer_list)
print(f"Highest value: {highest_value}")
print(f"Lowest value: {lowest_value}")

#Sorting the elements according to the ascending order
sorted_ascending= sorted(integer_list)
print("Sorted in ascending order: ", sorted_ascending)

#Sorting the elements according to the descending order
sorted_descending= sorted(integer_list, reverse= True)
print("Sorted in descending order: ", sorted_descending)

#Appending the two elements
integer_list.append(11)
integer_list.append(0)

#Printing the lists after appending
print("List after appending two elements:", integer_list)
