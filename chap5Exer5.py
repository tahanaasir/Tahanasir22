#Exercise 5: Playing around in class ☑️
#Use this exercise to play around with creating and accessing class members and methods.
#Develop a GUI using Tkinter to Create a class called Animal

#Give the class at least the following members Type, Name, Colour, Age, Weight, Noise
#The class should have the following methods sayHello() - says its name via print,makeNoise()
#-make an appropriate noise via print, animalDetails() -output all the details of the animal object
#Instantiate at least two objects from your animal class (e.g. Dog, Cow)
#Set values for each of the variables
#Invoke each of the class functions

import tkinter as tk

class Animal:
    def __init__(self, type_, name, colour, age, weight, noise):
        #Constructor to initializing the object with input values
        self.Type = type_
        self.Name = name
        self.Colour = colour
        self.Age = age
        self.Weight = weight
        self.Noise = noise

    def sayHello(self):
        #Method to say the name of the animal
        print(f"Hello, I am {self.Name}!")

    def makeNoise(self):
        #Method to make an appropriate noise
        print(f"{self.Name} says: {self.Noise}!")

    def animalDetails(self):
        #Method to output all details of the animal object
        details = f"Type: {self.Type}\nName: {self.Name}\nColour: {self.Colour}\nAge: {self.Age}\nWeight: {self.Weight}\nNoise: {self.Noise}"
        print(details)
        return details

class AnimalApp:
    def __init__(self, root):
        #Initializing the Tkinter GUI
        self.root = root
        self.root.title("Animal Information")
        self.create_widgets()

        #Instantiate two Animal objects (e.g., Dog, Cow)
        self.dog = Animal("Dog", "Buddy", "Brown", 3, 15, "Woof")
        self.cow = Animal("Cow", "MooMoo", "White", 5, 600, "Moo")

    def create_widgets(self):
        #Creating buttons for each action
        self.say_hello_button = tk.Button(self.root, text="Say Hello", command=self.invoke_say_hello)
        self.say_hello_button.pack(pady=10)

        self.make_noise_button = tk.Button(self.root, text="Make Noise", command=self.invoke_make_noise)
        self.make_noise_button.pack(pady=10)

        self.animal_details_button = tk.Button(self.root, text="Animal Details", command=self.invoke_animal_details)
        self.animal_details_button.pack(pady=10)

    def invoke_say_hello(self):
        #Invoke sayHello() for each animal
        self.dog.sayHello()
        self.cow.sayHello()

    def invoke_make_noise(self):
        #Invoke makeNoise() for each animal
        self.dog.makeNoise()
        self.cow.makeNoise()

    def invoke_animal_details(self):
        #Invoke animalDetails() for each animal and display in the console
        details_dog = self.dog.animalDetails()
        details_cow = self.cow.animalDetails()
        print("\nDetails for Dog:\n", details_dog)
        print("\nDetails for Cow:\n", details_cow)

if __name__ == "__main__":
    #Running the Tkinter application
    root = tk.Tk()
    app = AnimalApp(root)
    root.mainloop()
