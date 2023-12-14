#Exercise 4: Draw Shape☑️
#Using tkinter module develop Gui to ask the user to select
#shapes like oval, rectangle, square, and triangle and draw the shape using canvas.

import tkinter as tk
from tkinter import ttk

class ShapeDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        #Canvas to draw shapes
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(padx=10, pady=10)

        #Dropdown for selecting shapes
        self.shape_var = tk.StringVar()
        shapes = ["Select Shape", "Oval", "Rectangle", "Square", "Triangle"]
        self.shape_var.set(shapes[0])
        shape_dropdown = ttk.Combobox(root, textvariable=self.shape_var, values=shapes, state="readonly")
        shape_dropdown.pack(pady=10)
        shape_dropdown.bind("<<ComboboxSelected>>", self.draw_selected_shape)

    def draw_selected_shape(self, event):
        selected_shape = self.shape_var.get()

        #Clearing the canvas
        self.canvas.delete("all")

        #Drawing the selected shape
        if selected_shape == "Oval":
            self.canvas.create_oval(50, 50, 350, 200, outline="black")
        elif selected_shape == "Rectangle":
            self.canvas.create_rectangle(50, 50, 350, 200, outline="black")
        elif selected_shape == "Square":
            self.canvas.create_rectangle(50, 50, 200, 200, outline="black")
        elif selected_shape == "Triangle":
            self.canvas.create_polygon(50, 200, 200, 50, 350, 200, outline="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root)
    root.mainloop()
