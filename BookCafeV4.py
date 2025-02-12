import json
import DeliveryServiceV2
import menu
import menu_and_book_optionsV3
# Besides the json, this ^ above also imports a bunch of our Python files so their functions can be called remotely.


# File paths for JSON storage.
data_files = {
    "menu": "menu_list.json",
    "books": "book-list.json",
    "customers": "customers.json",
    "customer_list": "customer_list.json"
}

#Two convenience functions for json.
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} if "customer_list" in file_path else []
 
def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

#Loads a bunch of jsons and assigns them variables.
def load_data():
    menu_items = {"food": load_json(data_files["menu"]), "drinks": load_json(data_files["menu"])}
    book_list = load_json(data_files["books"])
    customer_data = load_json(data_files["customers"])
    customer_list = load_json(data_files["customer_list"])
    return menu_items, book_list, customer_data, customer_list
 
#All these below functions print out the user's menu options, so we can quickly call them later.
def display_main_menu():
    print("1. Visit Cafe")
    print("2. Employee")
    print("3. Delivery System")
    print("4. Exit")
 
def employee_menu():
    print("1. Update Menu and Books")
    print("2. View Orders")
    print("3. Exit")
 
def delivery_menu():
    print("1. View All Active Orders")
    print("2. Add New Customer Order")
    print("3. Exit")
 
#The core of our whole program!
def main():
    menu_items, book_list, customer_data, customer_list = load_data()
    customer_number = len(customer_list)  # Keeps track of customer entries
    while True:
        display_main_menu()
        user_choice = input("Enter your choice: ")
        if user_choice == "1":  # Customer. Goes straight to menu.py's main loop.
            menu.main()
        elif user_choice == "2":  # Employee. Can go to either menu and book's editing features or deliveryservice's ViewDelivieries.
            while True:
                employee_menu()
                employee_choice = input("Enter your choice: ")
                if employee_choice == "1":
                    menu_and_book_optionsV3.employee_options()
                elif employee_choice == "2":
                    DeliveryServiceV2.ViewDeliveries()
                elif employee_choice == "3":
                    break
                else:
                    print("Invalid choice.")
        elif user_choice == "3":  # Delivery System. Goes straight to the DeliveryService file's loop.
            DeliveryServiceV2.DeliveryStart()
        elif user_choice == "4":  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()