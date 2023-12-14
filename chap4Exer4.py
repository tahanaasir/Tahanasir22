#Exercise 4: letter count ☑️
#Develop a GUI App that asks the user to enter a character,
#reads the contents of the sentences.txt file, and counts the occurrences of the letter.

import tkinter as tk
from tkinter import filedialog

class CharCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Counter")

        #Creating and setting up widgets
        self.create_widgets()

    def create_widgets(self):
        #Label and Entry for user to input a character
        self.char_label = tk.Label(self.root, text="Enter a character:")
        self.char_label.grid(row=0, column=0, padx=10, pady=10)

        self.char_entry = tk.Entry(self.root)
        self.char_entry.grid(row=0, column=1, padx=10, pady=10)

        #Button to open the file dialog and selecting the file
        self.file_button = tk.Button(self.root, text="Select File", command=self.open_file)
        self.file_button.grid(row=1, column=0, columnspan=2, pady=10)

        #Button to perform character count
        self.count_button = tk.Button(self.root, text="Count Occurrences", command=self.count_occurrences)
        self.count_button.grid(row=2, column=0, columnspan=2, pady=10)

        #Result Label to display the count
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def open_file(self):
        #Open file dialog to select a file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if file_path:
            with open(file_path, 'r') as file:
                #Reading the contents of the file and store it
                self.file_contents = file.read()

    def count_occurrences(self):
        #Get the character from the entry
        char_to_count = self.char_entry.get()

        #Checking if a file is selected and a character is entered
        if hasattr(self, 'file_contents') and char_to_count:
            #Count occurrences of the character
            char_count = self.file_contents.lower().count(char_to_count.lower())

            #Displaying the result
            self.result_label.config(text=f"Occurrences of '{char_to_count}': {char_count}")
        else:
            #Displaying an error if a file or character is missing
            self.result_label.config(text="Please select a file and enter a character.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharCounterApp(root)
    root.mainloop()
