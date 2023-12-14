#Exercise 3: Area Function☑️
#Develop a GUI application using tkinter that allows users to calculate and
#display the areas of various shapes, including circles, squares, and rectangles.
#The application should utilize a tabbed interface to organize the calculations for each shape.
#Each of the 3 functions should ask for the necessary information (e.g. lengths and/or angles and output the answer.

import tkinter as tk
from tkinter import ttk, messagebox
import math

class AreaCalculatingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Area Calculator")

        #Creating a notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(padx=10, pady=10)

        #Creating tabs for circle, square, and rectangle
        self.create_a_circle_tab()
        self.create_a_rectangle_tab()
        self.create_a_square_tab()

    def create_a_circle_tab(self):
        #Creating a circle tab
        circle_tab = ttk.Frame(self.notebook)

        #Circle radius entry
        ttk.Label(circle_tab, text="Enter Radius: ").grid(row=0, column=0, padx=0, pady=0)
        self.circle_radius_entry = ttk.Entry(circle_tab)
        self.circle_radius_entry.grid(row=0, column=1, padx=10, pady=10)

        #Calculating button for circle
        ttk.Button(circle_tab, text="Calculate the Area", command=self.calculate_the_area_of_circle).grid(row=1, column=0, columnspan=2, pady=10)

        #Add circle tab to notebook
        self.notebook.add(circle_tab, text="Circle")

    def calculate_the_area_of_circle(self):
        #Calculating the area of circle
        try:
            radius = float(self.circle_radius_entry.get())
            area = math.pi * radius ** 2
            messagebox.showinfo("Result", f"The area of the circle is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid numeric value for the radius")

    def create_a_square_tab(self):
        #Creating a square tab
        square_tab = ttk.Frame(self.notebook)

        #Length entry of sides of the square
        ttk.Label(square_tab, text="Enter the length of the square: ").grid(row=0, column=0, padx=10, pady=10)
        self.square_side_entry = ttk.Entry(square_tab)
        self.square_side_entry.grid(row=0, column=1, padx=10, pady=10)

        #Calculation button for square
        ttk.Button(square_tab, text="Calculate the area of square", command=self.calculate_the_area_of_square).grid(row=1, column=0, columnspan=2, pady=10)

        #Add square tab to notebook
        self.notebook.add(square_tab, text="Square")

    def calculate_the_area_of_square(self):
        #Calculating the area of square
        try:
            side_length = float(self.square_side_entry.get())
            area = side_length**2
            messagebox.showinfo("Result", f"The area of square is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter the valid numeric value for the side length.")

    def create_a_rectangle_tab(self):
        #Creating a rectangle tab
        rectangle_tab = ttk.Frame(self.notebook)

        #Rectangle sides entries
        ttk.Label(rectangle_tab, text="Enter the length of rectangle: ").grid(row=0, column=0, padx=10, pady=10)
        self.rectangle_length_entry = ttk.Entry(rectangle_tab)
        self.rectangle_length_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(rectangle_tab, text="Enter the width of rectangle: ").grid(row=1, column=0, padx=10, pady=10)
        self.rectangle_width_entry = ttk.Entry(rectangle_tab)
        self.rectangle_width_entry.grid(row=1, column=1, padx=10, pady=10)

        #Calculation button of rectangle
        ttk.Button(rectangle_tab, text="Calculate the area of rectangle", command=self.calculate_the_area_of_rectangle).grid(row=2, column=0, columnspan=2, pady=10)

        #Add rectangle to notebook
        self.notebook.add(rectangle_tab, text="Rectangle")

    def calculate_the_area_of_rectangle(self):
        #Calculating the area of rectangle
        try:
            length = float(self.rectangle_length_entry.get())
            width = float(self.rectangle_width_entry.get())
            area = length * width
            messagebox.showinfo("Result", f"The area of rectangle is: {area:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter the valid numeric values for the length and width.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AreaCalculatingApp(root)
    root.mainloop()
