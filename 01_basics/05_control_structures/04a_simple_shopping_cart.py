'''
This is a simple program to simulate a shopping cart
There are no debugging features.
The user actions are:
    1. Create a shopping cart
    2. Add items to the shopping cart
    3. Remove Items from the Shopping Cart
    4. Show the shopping list
    5. Quit application
    6. Not to forget we need to generate a menu for the user.

Programming video is on vimeo
https://vimeo.com/406771429
password: 12345

Will show how to handle exceptions and eradicate typeErrors, duplicates in another video.
'''



# Create a shopping cart
shopping_cart = [] #empty list to be filled up with items in the store

# Add items to the shopping cart
def addItems(item):
    shopping_cart.append(item)

# Remove Items from the Shopping Cart
def removeItem(item):
    shopping_cart.remove(item)

# Show the shopping list
def showList():
    for item in shopping_cart:
        print(item)

# Not to forget we need to generate a menu for the user.
def menu():
    print('''
        1. Add Item
        2. Remove Item
        3. Show List
        4. Quit Application
    ''')

def shopping_cart_application():
    menu()
    while True:
        choice = input("Enter Choice: ")
        if choice == "1":
            item_to_add = input("Enter Item: ")
            addItems(item_to_add)
            continue
        elif choice == "2":
            item_to_remove = input("Enter Item: ")
            removeItem(item_to_remove)
            continue
        elif choice == "3":
            showList()
            continue
        elif choice == "4":
            break
        else:
            menu()
            continue

if __name__ == "__main__":
    shopping_cart_application()
