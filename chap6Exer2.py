#Exercise 2: Numpy Array ☑️
#For the array a = [20,23,82,40,32,15,67,52] print the output of following

#find the indices of even numbers
#Sort the array
#Slice elements from index 3 to the end of the array
#Slice elements from index 0 to index 4
#print [32 15 67] using negative slicing

a = [20, 23, 82, 40, 32, 15, 67, 52]

#Finding the indices of even numbers
even_indices = [i for i, num in enumerate(a) if num % 2 == 0]
print("Indices of even numbers:", even_indices)

#Sortting the array
sorted_array = sorted(a)
print("Sorted array:", sorted_array)

#Slice elements from index 3 to the end of the array
slice_from_3 = a[3:]
print("Elements from index 3 to the end:", slice_from_3)

#Slice elements from index 0 to index 4
slice_from_0_to_4 = a[0:5]
print("Elements from index 0 to index 4:", slice_from_0_to_4)

#Printing [32, 15, 67] using negative slicing
negative_slice = a[-5:-2]
print("Using negative slicing to print [32, 15, 67]:", negative_slice)
