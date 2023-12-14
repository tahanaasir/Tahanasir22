#Exercise 1: Greeting App ☑️
#Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.
#In InputFrame, include the following:
#A title label in blue.
#An entry field for the user's name.
#A dropdown menu for selecting a color.
#An "Update Greeting" button.
#In DisplayFrame, include a label to display the personalized greeting.
#Initially, DisplayFrame is empty, when the user clicks the "Update Greeting"
#button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.
#Use different background colors for each frame.

import tkinter as tk
from tkinter import ttk

def update_the_greeting():
    #Asking user's name and selecting colors
    user_name= entry_name.get()
    selected_color= color_var.get()

    #Creating personalized greeting
    greeting_text= f"Hello there!, {user_name}"

    #Updating the label in Display frame with the personalized greeting and selected colors
    display_label.config(text=greeting_text, foreground=selected_color)


#Creating the main window
root= tk.Tk()
root.title= ("Greeting App")

#Input frame
input_frame= ttk.Frame(root, padding=10, style="Input.TFrame")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

title_label= ttk.Label(input_frame, text="Personalized Greeting", style="Title.TLabel")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

#Entry field for the user's name
entry_name= ttk.Entry(input_frame, width=20)
entry_name.grid(row=1, column=0, columnspan=2, pady=5)

#Menu for selecting the colors
color_var= tk.StringVar()
color_choices= ["yellow", "black", "orange", "green", "blue", "brown"]

#Greeting button
update_button= ttk.Button(input_frame, text="Update Greeting", command=update_the_greeting)
update_button.grid(row=3, column=0, columnspan=2, pady=10)

#Display Frame
display_frame= ttk.Frame(root, padding=10, style="Display.TFrame")
display_frame.grid(row=1, column=0, padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

#Label to display the personlized greeting
display_label= ttk.Label(display_frame, text="", style="Greeting.TLabel")
display_label.grid(row=0, column=0, pady=10)

#Styles for Input Frame, Display Frame and Labels
style= ttk.Style()

style.configure("Input.TFrame", background="#FFE4B5")
style.configure("Display.TFrame", background="#87CEEB")
style.configure("Title.TLabel", foreground="white", font=("Arial", 12, "bold"))
style.configure("Greeting.TLabel", font=("Arial", 15, "bold"))
root.mainloop()
