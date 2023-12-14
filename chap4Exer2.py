#Exercise 2: CountString ☑️
#The file sentences.txt has a list of string data.
#Develop a GUI App that finds out how many times the following string appears

#Hello my name is Peter Parker
#I love Python Programming
#Love
#Enemy


import tkinter as tk
from tkinter import filedialog


def count_occurrences(file_content, target_strings):
    counts = {string: file_content.lower().count(string.lower()) for string in target_strings}
    return counts


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            file_content = file.read()
            result = count_occurrences(file_content, target_strings)
            update_result_text(result)


def search():
    search_text = search_entry.get()
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    if search_text:
        result = count_occurrences(search_text, [search_text])
        for string, count in result.items():
            result_text.insert(tk.END, f"{string}: {count} occurrences\n")
    else:
        result_text.insert(tk.END, "Please enter a search string.")

    result_text.config(state=tk.DISABLED)


def update_result_text(result):
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    for string, count in result.items():
        result_text.insert(tk.END, f"{string}: {count} occurrences\n")
    result_text.config(state=tk.DISABLED)


#Defineing the target strings
target_strings = [
    "Hello my name is Peter Parker",
    "I love Python Programming",
    "Love",
    "Enemy"
]

#Creating the main window
app = tk.Tk()
app.title("String Occurrence Counter")

#Creating pack and widgets
open_button = tk.Button(app, text="Open File", command=open_file)
open_button.pack(pady=5)

search_label = tk.Label(app, text="Search:")
search_label.pack()

search_entry = tk.Entry(app, width=30)
search_entry.pack(pady=5)

search_button = tk.Button(app, text="Search", command=search)
search_button.pack(pady=5)

result_text = tk.Text(app, height=10, width=50, state=tk.DISABLED)
result_text.pack(pady=10)

#Running the main loop
app.mainloop()
