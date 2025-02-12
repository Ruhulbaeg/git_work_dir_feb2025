import json
 
menu = r"menu_list.json"
books = r"books_placeholder.json"
 
 
def employee_menu():
    # Placeholder employee menu function
    print("Returning to the employee menu")
 
# Ask which they would like to change
 
def employee_options():
    while True:
        options = input("""Would you like to update the menu or book options? \n 
            1. Books\n
            2. Menu\n
            3. Return\n          
            4. Exit\n
            Enter your choice: """)
        if options.lower() == "books" or options == "1":
            with open(books) as file_object: # Show books listed in the Json file
                print("Here are the books currently avaliable")
                for line in file_object:
                    print(line.strip())
            updateDict(books)
            print("Redirecting to Books file...")
        elif options.lower() == "menu" or options == "2":
            with open(menu) as file_object: # show the food menu
                print("Here is the food that is currently avaliable")
                for line in file_object:
                    print(line.strip())
            updateDict(menu)
            print("Redirecting to Menu file...")
        elif options.lower() == "return" or options == "3":
            print("Returning to the main menu")
            employee_menu()
            #Send the employee back to the main menu
        elif options.lower() == "exit" or options == "4":
            print("Exiting...")
            break
        else:  input("Please enter a valid option:")

 
 
'''Prompt the employee to choose if they want to update/add an item or 
remove an item or exit, if they choose exit the code should send them 
back to the options function they came from'''
 
 
def updateDict(filepath):
    with open(filepath, 'r') as dict_file:
        data = json.load(dict_file)
    choice = int(input("""Do you want to (1) add/update an item or (2) remove an item or (3) exit: (1, 2, or 3): """))
    if choice in [1, 2, 3]:
        if choice == 1:
            item_id = int(input("Please choose the id number of the item you wish to update: ")) # Grab the item id from menu
            item = next((item for item in data if item["id"] == item_id), None)
            if item: # Check if the item exists in the list
                print(f"{item_id} chosen") # Print the name of the associated item
                while True:
                    change_item = input("""What would you like to change?\n
                                        1. Item Name
                                        2. Item Price
                                        3. Item Category
                                        4. Cancel
                                        Enter your choice: """)
                    if change_item.lower() == "item name" or change_item == "1":
                        new_name = input("What would you like to change the name to?: ")
                        item['name'] = new_name
                    elif change_item.lower() == "item price" or change_item == "2":
                        new_price = float(input("What is the new price?: "))
                        item['price'] = new_price
                    elif change_item.lower == "item category" or change_item == "3":
                        new_category = input("What is the new category?: ")
                        item['category'] = new_category
                    elif change_item.lower == "cancel" or change_item == "4":
                        print("Cancelling...")
                        break
                    else : input("Please enter a valid option: ")
            else:
                print("ID not found in file")                
    elif choice == 2:
        item_id = int(input("Please choose the id number of the item you wish to remove: ")) # Grab the item id from menu
        item = next((item for item in data if item["id"] == item_id), None)
        if item:
                data.remove(item)
                print(f"Item {item_id} removed.")
        else:
                print("ID not found in file.")
    elif choice == 3:
        employee_options()
        return
    else:
        print("Invalid choice")
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
 
# Go back to the employee options
 
employee_options()