#Exercise 6: Arithmetic Operation ☑️
#Develop a GUI to perform Arithmetic Operations.

#Create a class ArithmeticOperations with the following
#a result variable to store the result after calculation
#a function Calculate() - To perform an arithmetic operation selected by the user.
#You can use Combobox to provide users with options to perform selected arithmetic
#operations and entry widgets for the values.

import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0  #Variable to store the result

    def calculate(self, operation, num1, num2):
        #Performing the selected arithmetic operation
        if operation == "Addition":
            self.result = num1 + num2
        elif operation == "Subtraction":
            self.result = num1 - num2
        elif operation == "Multiplication":
            self.result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                self.result = num1 / num2
            else:
                return "Cannot divide by zero"
        return self.result

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arithmetic Calculator")

        #Creating and setting up widgets
        self.create_widgets()

        #Creating an instance of ArithmeticOperations
        self.arithmetic_operations = ArithmeticOperations()

    def create_widgets(self):
        #Label and Entry for entering the first number
        self.num1_label = tk.Label(self.root, text="Enter Number 1:")
        self.num1_label.grid(row=0, column=0, padx=10, pady=10)

        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.grid(row=0, column=1, padx=10, pady=10)

        #Label and Entry for entering the second number
        self.num2_label = tk.Label(self.root, text="Enter Number 2:")
        self.num2_label.grid(row=1, column=0, padx=10, pady=10)

        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.grid(row=1, column=1, padx=10, pady=10)

        #ComboBox for selecting the arithmetic operation
        self.operation_label = tk.Label(self.root, text="Select Operation:")
        self.operation_label.grid(row=2, column=0, padx=10, pady=10)

        self.operation_combobox = ttk.Combobox(self.root, values=["Addition", "Subtraction", "Multiplication", "Division"])
        self.operation_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.operation_combobox.set("Addition")

        #Button to calculate and display the result
        self.calculate_button = tk.Button(self.root, text="Calculate", command=self.calculate_and_display)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        #Label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_and_display(self):
        #Getting input values from the user
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter numeric values.")
            return

        #Getting the selected operation from the ComboBox
        operation = self.operation_combobox.get()

        #Calculating and displaying the result
        result = self.arithmetic_operations.calculate(operation, num1, num2)
        self.result_label.config(text=f"Result: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
