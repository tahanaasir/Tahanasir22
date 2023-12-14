#Bonus Assessment Exercises
#Exercise A: Playing around in class - Extension
#In the above Exercise -Playing around in class ask the user
#to enter the values of the Animal

import tkinter as tk
from tkinter import filedialog

class AnimalCharacteristicsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animal Characteristics")

        self.characteristics = {}

        #Creating widgets
        self.name_label = tk.Label(root, text="Enter the name of the animal:")
        self.name_entry = tk.Entry(root)

        self.sound_label = tk.Label(root, text="Enter the sound the animal makes:")
        self.sound_entry = tk.Entry(root)

        self.color_label = tk.Label(root, text="Enter the color of the animal:")
        self.color_entry = tk.Entry(root)

        self.load_button = tk.Button(root, text="Load Characteristics", command=self.load_characteristics)
        self.display_button = tk.Button(root, text="Display Characteristics", command=self.display_characteristics)
        self.result_label = tk.Label(root, text="Characteristics will be displayed here.")

        #Grid layout
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.sound_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.sound_entry.grid(row=1, column=1, padx=10, pady=5)

        self.color_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.color_entry.grid(row=2, column=1, padx=10, pady=5)

        self.load_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.display_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def load_characteristics(self):
        #Getting values from entry widgets and store in self.characteristics
        name = self.name_entry.get()
        sound = self.sound_entry.get()
        color = self.color_entry.get()

        self.characteristics = {'Name': name, 'Sound': sound, 'Color': color}

        self.result_label.config(text="Characteristics loaded successfully.")

    def display_characteristics(self):
        if not self.characteristics:
            self.result_label.config(text="Please load characteristics first.")
            return

        #Displaying the characteristics
        result_text = f"Animal Characteristics:\n"
        for key, value in self.characteristics.items():
            result_text += f"{key}: {value}\n"

        self.result_label.config(text=result_text)

#Creating and running the Tkinter app
root = tk.Tk()
app = AnimalCharacteristicsApp(root)
root.mainloop()