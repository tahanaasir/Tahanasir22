#Exercise 5: Password Check ☑️
#Develop a GUI App to check the validity of a password given by
#the user in the entry widget. The password should satisfy the following criteria:

#Contain at least 1 letter between a and z
#Contain at least 1 number between 0 and 9
#Contain at least 1 letter between A and Z
#Contain at least 1 character from $, #, @
#Minimum length of password: 6
#Maximum length of password: 12
#Ask user to include a maximum of 5 passcode attempts.
#Each time the user enters an incorrect passcode, they should be prompted
#of how many passcode attempts remain. If there are 5 failed passcode
#attempts the while loop should break and inform the user that the authorities have been alerted!

import tkinter as tk
from tkinter import messagebox

class PasswordValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Validator")

        #Creating and setting up widgets
        self.create_widgets()

        #Initializing the attempts
        self.attempts = 0
        self.max_attempts = 5

    def create_widgets(self):
        #Label and Entry for user to input a password
        self.password_label = tk.Label(self.root, text="Enter Password:")
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        #Button to validate password
        self.validate_button = tk.Button(self.root, text="Validate Password", command=self.validate_password)
        self.validate_button.grid(row=1, column=0, columnspan=2, pady=10)

    def validate_password(self):
        #Getting the password from the entry
        password = self.password_entry.get()

        #Checking if the password meets the criteria
        if self.is_valid_password(password):
            messagebox.showinfo("Success", "Password is valid!")
            self.root.destroy()  # Close the window upon successful validation
        else:
            #Increment attempts and check if the maximum attempts are reached
            self.attempts += 1
            if self.attempts >= self.max_attempts:
                messagebox.showerror("Alert", "Maximum attempts reached! Authorities have been alerted!")
                self.root.destroy()  # Close the window
            else:
                remaining_attempts = self.max_attempts - self.attempts
                messagebox.showwarning("Invalid Password", f"Invalid password. {remaining_attempts} attempts remaining.")

    def is_valid_password(self, password):
        #Checking password criteria
        if (6 <= len(password) <= 12 and
                any(c.islower() for c in password) and
                any(c.isdigit() for c in password) and
                any(c.isupper() for c in password) and
                any(c in "$#@ " for c in password)):
            return True
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordValidatorApp(root)
    root.mainloop()
