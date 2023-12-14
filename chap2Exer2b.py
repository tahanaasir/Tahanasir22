#Exercise 2 b: Square Grid ☑️
#With the pack layout manager, Create the following labels
#inside the frames. A and B inside the left frame. C and D inside the right frame
#Using Pack() align A and C at the top and B and D at the
#bottom of the frames that contain them
#Support resizing. Use the ‘expand’ and ‘fill’ attributes of
#the pack method to make the labels grow and expand into the available space.
#Assign border value as 5 to the frames

#Importing a Tkinter module
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create the left and right frames with a border of 5
left = tk.Frame(root, bd=5)
right = tk.Frame(root, bd=5)
#Packing the left frame to the left side of the window
left.pack(side="left", fill="both", expand=True)
#Packing the right frame to the right side of the window
right.pack(side="right", fill="both", expand=True)

#  A, B in the left frame
label_a = tk.Label(left, text="A",background="dark blue")
label_b = tk.Label(left, text="B")
#Packing a label_a to the top of the left frame
label_a.pack(side="top", fill="both", expand=True)
#Packing a label_b to the bottom of the left frame
label_b.pack(side="bottom", fill="both", expand=True)

# C, D in the right frame
label_c = tk.Label(right, text="C")
label_d = tk.Label(right, text="D",background="dark blue")
#Packing a label_c to the top of the right frame
label_c.pack(side="top", fill="both", expand=True)
#Packing a label_d to the bottom of the right frame
label_d.pack(side="bottom", fill="both", expand=True)

root.mainloop()