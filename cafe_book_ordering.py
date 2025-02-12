import json

MENU_FILE = "menu_list.json"
BOOKS_FILE = "books_list.json"
ORDERS_FILE = "orders.json"

def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def display_menu():
    menu = load_data(MENU_FILE)
    books = load_data(BOOKS_FILE)
    
    print("\n--- Cafe Menu ---")
    for item in menu:
        print(f"{item['id']}: {item['name']} - £{item['price']}")
    
    print("\n--- Book Selection ---")
    for book in books:
        print(f"{book['id']}: {book['name']} - £{book['price']}")

def take_order():
    orders = load_data(ORDERS_FILE)
    customer_name = input("Enter your name: ")
    address = input("Enter delivery address: ")
    order_items = []
    
    while True:
        display_menu()
        item_id = input("Enter the ID of the item you want to order (or 'done' to finish): ")
        if item_id.lower() == 'done':
            break
        
        menu = load_data(MENU_FILE) + load_data(BOOKS_FILE)
        item = next((i for i in menu if str(i['id']) == item_id), None)
        
        if item:
            order_items.append(item)
            print(f"Added {item['name']} to your order.")
        else:
            print("Invalid ID, please try again.")
    
    total_price = sum(item['price'] for item in order_items)
    
    orders.append({"customer": customer_name, "address": address, "items": order_items, "total": total_price})
    save_data(ORDERS_FILE, orders)
    print(f"Order placed! Total: £{total_price}")

def update_menu(filepath):
    data = load_data(filepath)
    
    while True:
        choice = input("\nWould you like to:\n1. Add an item\n2. Remove an item\n3. Return to menu\nEnter choice: ")
        
        if choice == "1":
            item_id = max((item['id'] for item in data), default=0) + 1
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            category = input("Enter category: ")
            data.append({"id": item_id, "name": name, "price": price, "category": category})
            print("Item added successfully!")
        
        elif choice == "2":
            item_id = int(input("Enter the ID of the item to remove: "))
            item = next((i for i in data if i['id'] == item_id), None)
            if item:
                data.remove(item)
                print("Item removed successfully!")
            else:
                print("ID not found.")
        
        elif choice == "3":
            break
        
        else:
            print("Invalid choice, try again.")
        
        save_data(filepath, data)

def employee_menu():
    while True:
        choice = input("\nEmployee Menu:\n1. Update Cafe Menu\n2. Update Book List\n3. Exit\nEnter choice: ")
        if choice == "1":
            update_menu(MENU_FILE)
        elif choice == "2":
            update_menu(BOOKS_FILE)
        elif choice == "3":
            break
        else:
            print("Invalid choice, try again.")

def main():
    while True:
        choice = input("\nWelcome!\n1. View Menu\n2. Place Order\n3. Employee Menu\n4. Exit\nEnter choice: ")
        if choice == "1":
            display_menu()
        elif choice == "2":
            take_order()
        elif choice == "3":
            employee_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()