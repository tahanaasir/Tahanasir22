#Exercise 5: Calculator☑️
#Develop a GUI to perform basic arithmetic operations like addition,
#subtraction, multiplication, Division, and modulo division using buttons.
#You can ask the user to enter the values in entry widget and select the operation to be performed.

#Importing a Tkinter module
import tkinter as tk

def perform_the_operation():
    try:
        #Asking user to enter the value
        num1= float(entry_num1.get())
        num2= float(entry_num1.get())

        #Performing the selected option
        operation= operation_var.get()

        if operation == "Addition":
            result= num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2
        elif operation == "Modulo Division":
            result = num1 % num2
        else:
            result = "Invalid Operation"

        #Displaying the result
        result_label.config(text=f"Result: {result}")

    except ValueError:
        #Handling the invalid input (non-numeric values)
        result_label.config(text="Please enter valid numbers.")

#Creating the main window
root= tk.Tk()
root.title("Arithemetic calculator")

#Creating and placing widgets using the Grid geometry manager
label_num1 = tk.Label(root, text="Enter first number: ")
label_num2 = tk.Label(root, text="Enter second number: ")

entry_num1 = tk.Entry(root)
entry_num2 = tk.Entry(root)

#Variable to store the selected option
operation_var= tk.StringVar()
operation_var.set("Addition")

#Button for selecting the options
operation_label= tk.Label(root, text="Select Operation: ")
addition_radio= tk.Radiobutton(root, text="Addition", variable=operation_var, value="Addition")
subtraction_radio= tk.Radiobutton(root, text="Subtraction", variable=operation_var, value="Subtraction")
division_radio= tk.Radiobutton(root, text="Division", variable=operation_var, value="Division")
muliplication_radio= tk.Radiobutton(root, text="Multiplication", variable=operation_var, value="Multiplication")
modulo_division_radio= tk.Radiobutton(root, text="Modulo Division", variable=operation_var, value="Modulo Division")

result_label= tk.Label(root, text="Result: ")
calculate_button= tk.Button(root, text="Calculate", command=perform_the_operation)

#Grids layout
label_num1.grid(row=0, column=0, padx=10, pady=5)
label_num2.grid(row=1, column=0, padx=10, pady=5)
entry_num1.grid(row=0, column=1, padx=10, pady=5)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

operation_label.grid(row=2, column=0, columnspan=2, pady=5)
addition_radio.grid(row=3, column=0, columnspan=2, pady=2)
subtraction_radio.grid(row=4, column=0, columnspan=2, pady=2)
division_radio.grid(row=5, column=0, columnspan=2, pady=2)
muliplication_radio.grid(row=6, column=0, columnspan=2, pady=2)
modulo_division_radio.grid(row=7, column=0, columnspan=2, pady=2)

calculate_button.grid(row=8, column=0, columnspan=2, pady=10)
result_label.grid(row=9, column=0, columnspan=2)
root.mainloop()