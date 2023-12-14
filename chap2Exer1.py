#Exercise 1: Welcome ☑️
#Develop a GUI program to do the following using the tkinter module
#create a label to display the welcome message and change the label font style (font name, bold, size)
#Set the default window size
#Disable resizing the window
#Add background color to the Window.

import tkinter as tk

def changing_font_style(label):
    #Changing the font (font name, bold, size)
    font_style = ("Arial", 13, "bold")
    label.config(font=font_style)

def main():
    #Creating the main window
    window = tk.Tk()
    window.title("GUI Program")

    #Setting the default window size
    window.geometry("400x200")

    #Disabling resizing the window
    window.resizable(width=False, height=False)

    #Adding the background color to the window
    window.configure(bg="#e6e6e6")

    #Creating a label to display the welcome message
    welcome_label = tk.Label(window, text="Welcome to GUI Program!!!")
    welcome_label.pack(pady=20)   # Add padding

    #Changing the font style of the label
    changing_font_style(welcome_label)

    #Running the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()
