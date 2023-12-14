#Bonus Assessment Exercises
#Exercise A: Temperature Converter
#Develop a GUI that implements a temperature converter application
#using Tkinter, allowing users to convert between Celsius and Fahrenheit.

import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        #Geting the temperature value and selected unit from the entry and dropdown
        temperature = float(entry.get())
        unit = unit_var.get()

        #Performing the conversion
        if unit == "Celsius":
            result = (temperature * 9/5) + 32
            result_unit = "Fahrenheit"
        else:
            result = (temperature - 32) * 5/9
            result_unit = "Celsius"

        #Displaying the result in the label
        result_label.config(text=f"Result: {result:.2f} {result_unit}")

    except ValueError:
        # Handle invalid input (non-numeric)
        messagebox.showerror("Error", "Please enter a valid numeric temperature.")

#Creating the main window
window = tk.Tk()
window.title("Temperature Converter")

#Creating and set up widgets
label = tk.Label(window, text="Enter Temperature:")
entry = tk.Entry(window, width=10)
unit_var = tk.StringVar()
unit_var.set("Celsius")
unit_dropdown = tk.OptionMenu(window, unit_var, "Celsius", "Fahrenheit")
convert_button = tk.Button(window, text="Convert", command=convert_temperature)
result_label = tk.Label(window, text="Result:")

#Placing widgets using grid layout
label.grid(row=0, column=0, padx=10, pady=10)
entry.grid(row=0, column=1, padx=10, pady=10)
unit_dropdown.grid(row=0, column=2, padx=10, pady=10)
convert_button.grid(row=1, column=0, columnspan=3, pady=10)
result_label.grid(row=2, column=0, columnspan=3, pady=10)

#Startting the main loop
window.mainloop()
