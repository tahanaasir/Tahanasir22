#Exercise B: Locations List ☑️
#Using the list

#locations =['dubai','paris', 'switzerland', 'London', 'amsterdam', 'New York']

#Print the list and find the length of the list
#Use sorted() to print your list in alphabetical order without modifying the actual list.
#Show that your list is still in its original order by printing it.
#Use sorted() to print your list in reverse alphabetical order without changing the order
#of the original list
#Show that your list is still in its original order by printing it again.
#Use reverse() to change the order of your list.
#Print the list to show that its order has changed.
#Use sort() to change your list so it’s stored in alphabetical order.
#Print the list to show that its order has been changed.
#Use sort() to change your list so it’s stored in reverse alphabetical order.
#Print the list to show that its order has changed.

#Given list
locations = ['dubai', 'paris', 'switzerland', 'London', 'amsterdam', 'New York']

#Printing the original list and finding its length
print("Original List:", locations)
print("Length of the List:", len(locations))

#Using sorted to print the list in alphabetical order without modifying the actual list
sorted_locations = sorted(locations)
print("Sorted List (Alphabetical Order):", sorted_locations)

#Showing that the original list is still in its original order
print("Original List:", locations)

#Using sorted to print the list in reverse alphabetical order without changing the order of the original list
reverse_sorted_locations = sorted(locations, reverse=True)
print("Sorted List (Reverse Alphabetical Order):", reverse_sorted_locations)

#Showing that the original list is still in its original order
print("Original List:", locations)

#Using reverse to change the order of the original list
locations.reverse()
print("Reversed List:", locations)

#Using sort to change the list so it's stored in alphabetical order
locations.sort()
print("Sorted List (Alphabetical Order):", locations)

#Using sort to change the list so it's stored in reverse alphabetical order
locations.sort(reverse=True)
print("Sorted List (Reverse Alphabetical Order):", locations)
