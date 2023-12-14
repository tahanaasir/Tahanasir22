#Exercise 1: User information ☑️
#Develop a GUI App to create a file called bio.txt and write
#the following information to the file asking user to enter the values:
#Name Age Hometown Each piece of data should be on a new line Once the data has
#been written to the file, read the data from the file and output the data.

import tkinter as tk
from tkinter import messagebox

class BioInfoApp:
    def __init__(self, root):
        self.root= root
        self.root.title("Bio Information")

        #Labels and entery widgets for users to input
        tk.Label(root, text="Name: ").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry= tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Age: ").grid(row=1, column=0, padx=10, pady=5)
        self.age_entry= tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Hometown: ").grid(row=2, column=0, padx=10, pady=5)
        self.hometown_entry= tk.Entry(root)
        self.hometown_entry.grid(row=2, column=1, padx=5, pady=5)

        #Buttons for enterting and reasing data
        tk.Button(root, text="Write to file", command=self.write_to_file).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Read to file", command=self.read_from_file).grid(row=4, column=0, columnspan=2, pady=10)


    def write_to_file(self):
        #Getting user input
        name= self.name_entry.get()
        age= self.age_entry.get()
        hometown= self.hometown_entry.get()

        #Writting data to bio text
        with open("bio.txt", "w")as file:
            file.write(f"Name: {name}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Hometown: {hometown}\n")

        messagebox.showinfo("Write to file", "Data has been written to bio.txt")

    def read_from_file(self):
        try:
            #Reading data from bio text
            with open("bio.txt", "t") as file:
                date = file.read()

            #Displaying data in messagebox
            messagebox.showinfo("Read from file", "Data read from bio.txt:\n\n + data")
        except FileNotFoundError:
            messagebox.showerror("Error", "The file bio.txt does not exist. Please write data first.")

if __name__== "__main__":
    root = tk.Tk()
    app= BioInfoApp(root)
    root.mainloop()
