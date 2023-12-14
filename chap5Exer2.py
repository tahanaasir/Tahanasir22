#Exercise 2: Student Class ☑️
#Develop a GUI using Tkinter to Create a class called Students.
#The class should have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int)
#The class should have the following methods calcGrade() - should return an average from the three
#marks.display()- should output the student name and calculated grade average. Create one object using
#a constructor that contains parameters to initialize all of the variables. Ask user to input the variable
#values using input() and pass the values to the second object

import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        #Constructor to initialize the object with input values
        self.Name = name
        self.Mark1 = mark1
        self.Mark2 = mark2
        self.Mark3 = mark3

    def calcGrade(self):
        #Method to calculate the average grade
        return (self.Mark1 + self.Mark2 + self.Mark3) / 3

    def display(self):
        #Method to format and return student details with average grade
        average = self.calcGrade()
        return f"Name: {self.Name}\nAverage Grade: {average:.2f}"

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Calculator")

        #Creating and setting up widgets
        self.create_widgets()

    def create_widgets(self):
        #Label and Entry for user to input student details
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.mark1_label = tk.Label(self.root, text="Mark 1:")
        self.mark1_label.grid(row=1, column=0, padx=10, pady=10)

        self.mark1_entry = tk.Entry(self.root)
        self.mark1_entry.grid(row=1, column=1, padx=10, pady=10)

        self.mark2_label = tk.Label(self.root, text="Mark 2:")
        self.mark2_label.grid(row=2, column=0, padx=10, pady=10)

        self.mark2_entry = tk.Entry(self.root)
        self.mark2_entry.grid(row=2, column=1, padx=10, pady=10)

        self.mark3_label = tk.Label(self.root, text="Mark 3:")
        self.mark3_label.grid(row=3, column=0, padx=10, pady=10)

        self.mark3_entry = tk.Entry(self.root)
        self.mark3_entry.grid(row=3, column=1, padx=10, pady=10)

        #Button for calculating and displaying the average
        self.calculate_button = tk.Button(self.root, text="Calculate Average", command=self.calculate_and_display)
        self.calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_and_display(self):
        #Getting input values from the user
        name = self.name_entry.get()
        try:
            mark1 = float(self.mark1_entry.get())
            mark2 = float(self.mark2_entry.get())
            mark3 = float(self.mark3_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for marks.")
            return

        #Creating a Students object using the constructor
        student1 = Students(name, mark1, mark2, mark3)

        #Displaying student details and average grade
        result = student1.display()
        messagebox.showinfo("Result", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
