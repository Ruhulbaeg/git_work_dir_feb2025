import json
 
menu = r"menu_list.json"
books = r"book-list.json"
def employee_menu():
    print("Returning to the employee menu")
    employee_options()  # Now we redirect back to options
 

def employee_options():
    menuAndBookMode = True
    while menuAndBookMode == True:
        options = input("""Would you like to update the menu or book options? \n 
            1. Books\n
            2. Menu\n
            3. Return\n          
            4. Exit\n
            Enter your choice: """)
        if options.lower() == "books" or options == "1":
            with open(books) as file_object:
                print("Here are the books currently available:")
                for line in file_object:
                    print(line.strip())
            updateDict(books)
            print("Redirecting to Books file...")
        elif options.lower() == "menu" or options == "2":
            with open(menu) as file_object:
                print("Here is the food that is currently available:")
                for line in file_object:
                    print(line.strip())
            updateDict(menu)
            print("Redirecting to Menu file...")
        elif options.lower() == "return" or options == "3":
            employee_menu()
            menuAndBookMode = False
        elif options.lower() == "exit" or options == "4":
            print("Exiting...")
            menuAndBookMode = False
        else:
            print("Please enter a valid option.")
 
def updateDict(filepath):
    with open(filepath, 'r') as dict_file:
        data = json.load(dict_file)
 
    choice = int(input("""Do you want to:\n
        1. Add a new item\n
        2. Update an existing item\n
        3. Remove an item\n
        4. Exit\n
        Enter your choice (1, 2, 3, or 4): """))
    if choice == 1:  # **Adding a new item**
        new_id = int(input("Enter a unique ID for the new item: "))
        existing_ids = [item["id"] for item in data]
 
        if new_id in existing_ids:
            print("Error: ID already exists! Try again with a unique ID.")
        else:
            new_name = input("Enter the item name: ")
            new_price = float(input("Enter the item price: "))
            new_category = input("Enter the item category: ")
 
            new_item = {
                "id": new_id,
                "name": new_name,
                "price": new_price,
                "category": new_category
            }
            data.append(new_item)
            print(f"New item '{new_name}' added successfully!")
 
    elif choice == 2:  # **Updating an item**
        item_id = int(input("Enter the ID number of the item you wish to update: "))
        item = next((item for item in data if item["id"] == item_id), None)
        if item:
            print(f"{item_id} chosen")
            while True:
                change_item = input("""What would you like to change?\n
                    1. Item Name
                    2. Item Price
                    3. Item Category
                    4. Cancel
                    Enter your choice: """)
                if change_item == "1":
                    new_name = input("Enter the new name: ")
                    item['name'] = new_name
                elif change_item == "2":
                    new_price = float(input("Enter the new price: "))
                    item['price'] = new_price
                elif change_item == "3":
                    new_category = input("Enter the new category: ")
                    item['category'] = new_category
                elif change_item == "4":
                    print("Cancelling...")
                    break
                else:
                    print("Please enter a valid option.")
        else:
            print("ID not found in file.")
 
    elif choice == 3:  # **Removing an item**
        item_id = int(input("Enter the ID number of the item you wish to remove: "))
        item = next((item for item in data if item["id"] == item_id), None)
        if item:
            data.remove(item)
            print(f"Item {item_id} removed successfully.")
        else:
            print("ID not found in file.")
 
    elif choice == 4:
        employee_options()
        return
 
    else:
        print("Invalid choice")
 
    # **Save the updated data back to the JSON file**
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)