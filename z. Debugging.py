
# Find all the errors in this program and correct them. The program should be error free and run without any issues.

menu = {"burger": 5.00, "fries": 2.00, "cheeseburger": 6.00, "nuggets": 4.00, "ice_cream": 3.00}

def menu_and_cost(choice):
    """Determine if user choice is on the menu. Returns `True` if it is else return `False`"""
    if choice in menu.keys():
         return f"Your choice is on the menu and price of it is {menu[choice]}"
    else:
        return "Your choice is not on the menu and we don't serve that"



# Ask the user what they would like to eat
choice = input ("What would you like to order? ")

print(menu_and_cost(choice))
