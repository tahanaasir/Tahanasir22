#Exercise 3: Line graph ☑️
#Draw a line in a diagram from position (1, 2) to position (6, 8)
#Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1)
#and finally to position (8, 10)

import matplotlib.pyplot as plt

#Drawing a line from (1, 2) to (6, 8)
x_line = [1, 6]
y_line = [2, 8]

#Drawing a dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
x_dotted_line = [1, 2, 6, 8]
y_dotted_line = [3, 8, 1, 10]

#Plotting the line
plt.plot(x_line, y_line, label='Line')

#Plotting the dotted line
plt.plot(x_dotted_line, y_dotted_line, 'ro--', label='Dotted Line')

#Setting axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line and Dotted Line in Diagram')

#Displaying the legend
plt.legend()

#Showing the plot
plt.show()
