#Exercise A: Petrol Price
#Every time a motorist buys some petrol, he notes the number of liters bought
#and the amount paid per liter. This data can be found in the petrolPrice.txt
#file in your GitHub repository.The data is stored in columns separated by a
#tabbed space, like the following sample:

#Liters	cost
#20.0	  56.40
#9.6	  29.95
#5.0	  15.60
#15.0	  54.30
#18.4	  65.32
#18.7	  75.36
#17.7	  80.00
#Develop a GUI App that calculates:

#What was the cost of petrol per liter bought?
#What was the overall average price per liter of petrol bought?
#How much petrol in liters was bought at under 3.5AED per liter?

import tkinter as tk
from tkinter import filedialog

class PetrolCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Petrol Price Calculator")

        self.data = None

        #Creating widgets
        self.load_button = tk.Button(root, text="Load Data", command=self.load_data)
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.result_label = tk.Label(root, text="Results will be displayed here.")

        #Grid layout
        self.load_button.grid(row=0, column=0, padx=10, pady=10)
        self.calculate_button.grid(row=1, column=0, padx=10, pady=10)
        self.result_label.grid(row=2, column=0, padx=10, pady=10)

    def load_data(self):
        #Opening a file dialog to choose the data file
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            #Reading data from the file and store it in self.data
            with open(file_path, 'r') as file:
                lines = file.readlines()
                #Skipping the header line
                header = lines[0].strip().split('\t')
                self.data = [tuple(map(float, line.strip().split('\t'))) for line in lines[1:]]

            self.result_label.config(text="Data loaded successfully.")

    def calculate(self):
        if not self.data:
            self.result_label.config(text="Please load data first.")
            return

        #Calculating requested values
        total_cost = sum(cost for liters, cost in self.data)
        total_liters = sum(liters for liters, cost in self.data)
        cost_per_liter = total_cost / total_liters if total_liters != 0 else 0

        average_price_per_liter = total_cost / len(self.data) if len(self.data) != 0 else 0

        under_3_5_liters = sum(liters for liters, cost in self.data if cost / liters < 3.5)

        #Displaying the results
        result_text = f"Cost of petrol per liter bought: {cost_per_liter:.2f} AED\n"
        result_text += f"Overall average price per liter: {average_price_per_liter:.2f} AED\n"
        result_text += f"Petrol bought at under 3.5 AED per liter: {under_3_5_liters:.2f} liters"

        self.result_label.config(text=result_text)

#Creating and running the Tkinter app
root = tk.Tk()
app = PetrolCalculatorApp(root)
root.mainloop()