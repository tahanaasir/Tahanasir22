#Exercise 11: Year Tuples☑️
#Create a tuple with values
#year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)
#Access the value at index -3
#Reverse the tuple and print the original tuple and reversed tuple
#Count number of times 2009 is in the tuple (use count() method)
#Get the index value of 2018(Use index method)
#Find length of given tuple(Use len() method)

#Defining the tuple
year= (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

#Accessing the value at index -3
value_at_indux_minus_3= year[-3]
print("Value at index -3: ", value_at_indux_minus_3)

#Reversing the tuple
reversed_year= tuple(reversed(year))
print("Original tuple: ", year)
print("Reversed tuple: ", reversed_year)

#Counting the year 2009 in the tuple
count_2009= year.count(2009)
print(("Number of times 2009 has been repeated in tuple: ", count_2009))

#Getting the indux value of 2018
index_2018= year.index(2018)
print("Index of 2018: ", index_2018)

#Finding the length of the tuple
tuple_lenght= len(year)
print("Lenght of tuple is: ", tuple_lenght)
