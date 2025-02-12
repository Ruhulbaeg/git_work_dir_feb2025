import json
import DeliveryServiceV2

#Grabs the food of the json!
menu_items = r'menu_list.json'
with open(menu_items, 'r') as json_file:
    foodMenu = json.load(json_file)
#The second json for the books!
book_items = r'book-list.json'
with open(book_items, 'r') as json_file:
    books = json.load(json_file)

orders = []

#"type" is a string, either 'food' or 'books'. Because both lists are formatted in the same way (thanks to Hamza!) they can be displayed in pretty much the same way.
#Oh yeah, and this function displays the menu.
def display_menu(type):
    if type == "food":
        print("\n--- Cafe Menu ---")
        for item in foodMenu:
            print(f"{item['id']}. {item['name']} - £{item['price']} ({item['category']})")
    elif type == "books":
        print("\n--- Books ---")
        for item in books:
            print(f"{item['id']}. {item['name']} - £{item['price']} ({item['category']})")
    print("-----------------\n")
 
def place_order(type):
    #These variables need to be global so Python can keep track of them
    global foodMenu
    global books
    display_menu(type)
    order_items = []
    # 'menu' is made equal to either foodMenu or books, and the algorithm can apply equally to menu from here on and will work in both cases.
    if type == "food":
        menu = foodMenu
    if type == "books":
        menu = books
    while True:
        item_id = input("Enter the item ID to order (or 'done' to finish): ")
        if item_id.lower() == "done":
            break
        try:
            item_id = int(item_id)
            item = next((i for i in menu if i["id"] == item_id), None)
            if item:
                order_items.append(item)
                print(f"Added {item['name']} to your order.")
            else:
                print("Invalid item ID. Try again.")
        except ValueError:
            print("Please enter a valid number.")
 
    if not order_items:
        print("No items selected. Returning to menu.")
        return
    #Because the inputs were already here, I made a "QuickOrder" function on DeliveryService that can have these values inserted into it from outside, and it will take care of the rest.
    name = input("Enter your name: ")
    address = input("Enter delivery address: ")
    DeliveryServiceV2.QuickOrder(name, order_items, address)
    #Recaps everything that just happened for the customer.
    print("\nOrder placed successfully!")
    print(f"Customer: {name}")
    print(f"Delivery Address: {address}")
    print("Ordered Items:")
    for item in order_items:
        print(f"- {item['name']} (£{item['price']})")

#The bit that employees can enter to tweak things about the menu.
def manage_menu():
    global foodMenu
    global books
    while True:
        print("\n--- Manage Cafe Menu ---")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Remove Item")
        print("4. View Menu")
        print("5. Go Back")
 
        choice = input("Select an option: ")
        #The system for creating a completely new menu item. Gets three inputs and makes them its values.
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            category = input("Enter category (Food/Drink): ")
 
            new_id = max(item["id"] for item in foodMenu) + 1
            foodMenu.append({"id": new_id, "name": name, "price": price, "category": category})
            with open(menu_items, 'w') as json_file:
                json.dump(foodMenu,json_file)
            print(f"{name} added to the menu!")
        #Editing an existing item.
        elif choice == "2":
            display_menu('food')
            item_id = int(input("Enter item ID to edit: "))
            item = next((i for i in foodMenu if i["id"] == item_id), None)
            #Gets three inputs like last time, but ALSO displays the current values for convenience's sake.
            if item:
                item["name"] = input(f"New name ({item['name']}): ") or item["name"]
                item["price"] = float(input(f"New price (£{item['price']}): ") or item["price"])
                item["category"] = input(f"New category ({item['category']}): ") or item["category"]
                with open(menu_items, 'w') as json_file:
                    json.dump(foodMenu,json_file)
                print("Item updated successfully!")
            else:
                print("Item not found.")
        #Removing an existing item, this is quite short and simple.
        elif choice == "3":
            display_menu('food')
            item_id = int(input("Enter item ID to remove: "))
            foodMenu
            foodMenu = [item for item in foodMenu if item["id"] != item_id]
            #Edits the json to reflect the newly edited menu
            with open(menu_items, 'w') as json_file:
                json.dump(foodMenu,json_file)
            print("Item removed.")
 
        elif choice == "4":
            display_menu('food')
 
        elif choice == "5":
            break
 
        else:
            print("Invalid choice. Try again.")

#This is the core function that has all the cafe's functionality in one place. Depending on user input, this will call the other functions that are above.
def main():
    while True:
        print("\nWelcome to the Bookshop Cafe")
        print("1. View Menu")
        print("2. Place an Order")
        print("3. Manage Menu (Employees Only)")
        print("4. Exit")
 
        choice = input("Select an option: ")
 
        if choice == "1":
            display_menu("food")
            display_menu("books")
        elif choice == "2":
            customerInput = input("What would you like to order? Type 'books' or 'food'.")
            #Distinguishes between what the customer wants, whether that be food or books.
            if customerInput == "food":
                place_order("food")
            elif customerInput == "books":
                place_order('books')
            else:
                print("Error, we aren't sure what you typed!")
        elif choice == "3":
            manage_menu()
        elif choice == "4":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice, please try again.")
 
#This last bit is just for debugging- If menu.py is run by itself, it will run main(), if not this won't do anything.
if __name__ == "__main__":
    main()