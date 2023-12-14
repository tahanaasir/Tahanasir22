#Bonus Assessment Exercise - Burger Shack Vendor
#Burger Shack is about to open in RAK, however, the fast food chain is in
#need of an ordering system. Write a program to handle the ordering process for the burger shack.
#The program should include:

#The ability to choose between at least three burger types (e.g. Beef, Chicken, Vegetarian)
#The ability to add toppings, with at least three to choose from (e.g. cheese, peanut butter, avocado)
#The ability to add condiments, with at least three to choose from (e.g. ketchup, mayonnaise, bbq sauce)
#The ability to add sides, these can include items such as fries and drinks.
#The ability to handle payment and return change to the user
#You should design your program to make use of functions and pass information to and
#from these as appropriate. Alongside the above requirements, you are free to extend
#the functionality of the program as you see fit.

def display_menu():
    #Displaying the available burger types
    print("Burger Types:")
    print("1. Beef Burger")
    print("2. Chicken Burger")
    print("3. Vegetarian Burger")

def choose_burger():
    #Getting user input for choosing a burger type
    choice = input("Enter the number of the burger type you want: ")
    return choice

def choose_toppings():
    #Displaying and getting user input for choosing toppings
    print("\nChoose Toppings:")
    print("1. Cheese")
    print("2. Peanut Butter")
    print("3. Avocado")
    toppings = input("Enter the numbers of toppings separated by commas (e.g., 1,2): ")
    return toppings.split(',')

def choose_condiments():
    #Displaying and getting user input for choosing condiments
    print("\nChoose Condiments:")
    print("1. Ketchup")
    print("2. Mayonnaise")
    print("3. BBQ Sauce")
    condiments = input("Enter the numbers of condiments separated by commas (e.g., 1,2): ")
    return condiments.split(',')

def choose_sides():
    #Displaying and getting user input for choosing sides
    print("\nChoose Sides:")
    print("1. Fries")
    print("2. Drink")
    sides = input("Enter the numbers of sides separated by commas (e.g., 1,2): ")
    return sides.split(',')

def calculate_total(order_items):
    #Calculating the total cost based on the chosen items
    prices = {
        'burger': 5.00,
        'topping': 1.00,
        'condiment': 0.50,
        'side': 2.00
    }

    total = 0
    for item_type, choices in order_items.items():
        total += len(choices) * prices[item_type]

    return total

def handle_payment(total):
    #Handling payment and providing change information
    amount_paid = float(input(f"\nThe total amount is ${total:.2f}. Enter the amount paid: "))
    change = amount_paid - total

    if change >= 0:
        print(f"Thank you for your payment! Your change is ${change:.2f}.")
    else:
        print("Insufficient payment. Please provide enough funds.")

def main():
    #Initializing the order_items dictionary to store user choices
    order_items = {}

    #Displaying the menu and guide the user through the ordering process
    display_menu()

    #Asking user to choose the burger type
    burger_choice = choose_burger()
    order_items['burger'] = burger_choice

    #Asking user to choose there toppings
    order_items['topping'] = choose_toppings()
    order_items['condiment'] = choose_condiments()
    order_items['side'] = choose_sides()

    #Calculating the total and handling payment
    total = calculate_total(order_items)
    handle_payment(total)

if __name__ == "__main__":
    main()
