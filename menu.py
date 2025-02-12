import json

# menu = [
#      {"id": 1, "name": "Coffee", "price": 2.50, "category": "Drink"},
#      {"id": 2, "name": "Tea", "price": 2.00, "category": "Drink"},
#      {"id": 3, "name": "Sandwich", "price": 5.00, "category": "Food"},
#      {"id": 4, "name": "Cake", "price": 3.50, "category": "Food"},
#      {"id": 5, "name": "Crossaint", "price": 1.50, "category":"Food"},
#      {"id": 6, "name": "Coke", "price": 1.80, "category":"Drink"}
#  ]

#grabs what it needs out of the json!
menu_items = r'menu_list.json'
with open(menu_items, 'r') as json_file:
    menu = json.load(json_file)


orders = []


def display_menu():
    print("\n--- Cafe Menu ---")
    for item in menu:
        print(f"{item['id']}. {item['name']} - £{item['price']} ({item['category']})")
    print("-----------------\n")
 
def place_order():
    global menu
    display_menu()
    order_items = []
   
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
 
    name = input("Enter your name: ")
    address = input("Enter delivery address: ")
 
    new_order = {"name": name, "items": order_items, "address": address}
    orders.append(new_order)
 
    print("\nOrder placed successfully!")
    print(f"Customer: {name}")
    print(f"Delivery Address: {address}")
    print("Ordered Items:")
    for item in order_items:
        print(f"- {item['name']} (£{item['price']})")
 
def manage_menu():
    global menu
    while True:
        print("\n--- Manage Cafe Menu ---")
        print("1. Add Item")
        print("2. Edit Item")
        print("3. Remove Item")
        print("4. View Menu")
        print("5. Go Back")
 
        choice = input("Select an option: ")
 
        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            category = input("Enter category (Food/Drink): ")
 
            new_id = max(item["id"] for item in menu) + 1
            menu.append({"id": new_id, "name": name, "price": price, "category": category})
            with open(menu_items, 'w') as json_file:
                json.dump(menu,json_file)
            print(f"{name} added to the menu!")
 
        elif choice == "2":
            display_menu()
            item_id = int(input("Enter item ID to edit: "))
            item = next((i for i in menu if i["id"] == item_id), None)
 
            if item:
                item["name"] = input(f"New name ({item['name']}): ") or item["name"]
                item["price"] = float(input(f"New price (£{item['price']}): ") or item["price"])
                item["category"] = input(f"New category ({item['category']}): ") or item["category"]
                with open(menu_items, 'w') as json_file:
                    json.dump(menu,json_file)
                print("Item updated successfully!")
            else:
                print("Item not found.")
 
        elif choice == "3":
            display_menu()
            item_id = int(input("Enter item ID to remove: "))
            menu
            menu = [item for item in menu if item["id"] != item_id]
            #Edits the json to reflect the newly edited menu
            with open(menu_items, 'w') as json_file:
                json.dump(menu,json_file)
            print("Item removed.")
 
        elif choice == "4":
            display_menu()
 
        elif choice == "5":
            break
 
        else:
            print("Invalid choice. Try again.")
       
def main():
    while True:
        print("\nWelcome to the Bookshop Cafe")
        print("1. View Menu")
        print("2. Place an Order")
        print("3. Manage Menu (Employees Only)")
        print("4. Exit")
 
        choice = input("Select an option: ")
 
        if choice == "1":
            display_menu()
        elif choice == "2":
            place_order()
        elif choice == "3":
            manage_menu()
        elif choice == "4":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice, please try again.")
 
if __name__ == "__main__":
    main()