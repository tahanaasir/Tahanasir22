#Exercise 4: Shapes ☑️
#Develop a GUI using Tkinter to calculate the area of Shapes.
#Create a parent class called Shape. This should have the following methods inputSides() –
#Ask the user to enter the sides of the shape. Now create subclasses for a circle, rectangle, and triangle.
#These should include an appropriate  area() method that will use the side values from the shape class.

import tkinter as tk
from tkinter import messagebox
import math

class Shape:
    def __init__(self, master):
        self.master = master
        self.master.title("Shape Area Calculator")

        #Creating and setting up widgets
        self.create_widgets()

    def create_widgets(self):
        #Label and Entry for user to input sides
        self.side_label = tk.Label(self.master, text="Enter Side(s):")
        self.side_label.grid(row=0, column=0, padx=10, pady=10)

        self.side_entry = tk.Entry(self.master)
        self.side_entry.grid(row=0, column=1, padx=10, pady=10)

        #Button to calculate and to display area
        self.calculate_button = tk.Button(self.master, text="Calculate Area", command=self.calculate_area)
        self.calculate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def inputSides(self):
        #Method to get the side values from the user
        sides = self.side_entry.get()
        return [float(side) for side in sides.split()]

    def calculate_area(self):
        #Abstract method for calculating the area, to be implemented in subclasses
        pass

class Circle(Shape):
    def calculate_area(self):
        # Calculating the area of a circle by using a formula: A = π * r^2
        try:
            radius = self.inputSides()[0]
            area = math.pi * (radius ** 2)
            messagebox.showinfo("Result", f"Area of Circle: {area:.2f}")
        except (ValueError, IndexError):
            messagebox.showerror("Error", "Please enter a valid radius.")

class Rectangle(Shape):
    def calculate_area(self):
        #Calculating the area of a rectangle by using a formula: A = length * width
        try:
            sides = self.inputSides()
            area = sides[0] * sides[1]
            messagebox.showinfo("Result", f"Area of Rectangle: {area:.2f}")
        except (ValueError, IndexError):
            messagebox.showerror("Error", "Please enter valid length and width.")

class Triangle(Shape):
    def calculate_area(self):
        #Calculating the area of a triangle by using Heron's formula
        try:
            sides = self.inputSides()
            s = sum(sides) / 2
            area = math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))
            messagebox.showinfo("Result", f"Area of Triangle: {area:.2f}")
        except (ValueError, IndexError):
            messagebox.showerror("Error", "Please enter valid side lengths.")

if __name__ == "__main__":
    root = tk.Tk()

    #Creating instances of the subclasses
    circle_app = Circle(root)
    rectangle_app = Rectangle(root)
    triangle_app = Triangle(root)

    root.mainloop()
