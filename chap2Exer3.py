#Exercise 3: Login page ☑️
#Create a login page using the Grid geometry.

#Importing a Tkinter module
import tkinter as tk

def on_the_login():
    username= enter_username.get()
    password= enter_password.get()

    #Adding the authentication login here
    print(f"Username: {username}/nPassword: {password}")

#Creating the main window
root= tk.Tk()
root.title("Login Page")

#Creating and placing widgets using the Grid geomatery manager
label_username= tk.Label(root, text="Username: ")
label_password=  tk.Label(root, text="Password: ")

enter_username = tk.Entry(root)
enter_password = tk.Entry(root, show="*")

button_login= tk.Button(root, text="login", command=on_the_login())

label_username.grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)
label_password.grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
enter_username.grid(row=0, column=1, padx=10, pady=5)
enter_password.grid(row=1, column=1, padx=10, pady=5)
button_login.grid(row=2, column=1, pady=10)

root.mainloop()