#Exercise 2: Coffee Vending Machine☑️
#Develop a coffee Vending Machine that asks users to select the type of coffee,
#and also prompts users to select various options like sugar, milk, etc. Once selected
#display the message using a message box. Also, use images in the app.

import tkinter as tk
from tkinter import messagebox

class CoffeeVendingMachine:
    def __init__(self, root):
        # Initialize the CoffeeVendingMachine
        self.root = root
        self.root.title("Coffee Vending Machine")

        # Coffee type options
        self.coffee_options = {
            "Black Coffee": None,
            "Latte": None,
            "Cappuccino": None
        }

        # Variables to track milk and sugar options
        self.milk_var = tk.BooleanVar()
        self.sugar_var = tk.BooleanVar()

        # Set up the graphical user interface
        self.create_gui()

    def create_gui(self):
        # Coffee type label
        tk.Label(self.root, text="Select Coffee Type:").pack()

        # Coffee type options (Radiobuttons)
        for coffee_type in self.coffee_options.keys():
            tk.Radiobutton(self.root, text=coffee_type, variable=tk.StringVar(), value=coffee_type,
                           command=lambda t=coffee_type: self.show_options(t)).pack()

        # Milk option (Checkbutton)
        tk.Checkbutton(self.root, text="Add Milk", variable=self.milk_var).pack()

        # Sugar option (Checkbutton)
        tk.Checkbutton(self.root, text="Add Sugar", variable=self.sugar_var).pack()

        # Order button
        tk.Button(self.root, text="Place Order", command=self.place_order).pack()

    def show_options(self, coffee_type):
        # Display the selected coffee type (you can add image code here if needed)
        pass

    def place_order(self):
        # Get selected coffee type
        selected_coffee_value = self.selected_coffee.get()

        # Determine milk and sugar options
        add_milk = "with Milk" if self.milk_var.get() else "without Milk"
        add_sugar = "with Sugar" if self.sugar_var.get() else "without Sugar"

        # Display order confirmation in a message box
        order_message = f"You have ordered {selected_coffee_value} {add_milk} {add_sugar}. Enjoy your coffee!"
        messagebox.showinfo("Order Confirmation", order_message)


if __name__ == "__main__":
    # Create and run the Tkinter application
    root = tk.Tk()
    app = CoffeeVendingMachine(root)
    root.mainloop()
