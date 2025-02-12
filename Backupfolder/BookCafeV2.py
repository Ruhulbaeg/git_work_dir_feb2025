import json
import DeliveryService

# File paths for JSON storage
data_files = {
    "menu": "menu.json",
    "books": "books.json",
    "customers": "customers.json",
    "customer_list": "customer_list.json"
}
 
def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {} if "customer_list" in file_path else []
 
def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
 
def load_data():
    menu_items = {"food": load_json(data_files["menu"]), "drinks": load_json(data_files["menu"])}
    book_list = load_json(data_files["books"])
    customer_data = load_json(data_files["customers"])
    customer_list = load_json(data_files["customer_list"])
    return menu_items, book_list, customer_data, customer_list
 
def display_main_menu():
    print("1. Customer")
    print("2. Employee")
    print("3. Delivery System")
    print("4. Exit")
 
def customer_menu():
    print("1. View Menu and Books")
    print("2. Order Items")
    print("3. Exit")
 
def employee_menu():
    print("1. Update Menu and Books")
    print("2. Update Specials")
    print("3. View Orders")
    print("4. Exit")
 
def delivery_menu():
    print("1. View All Active Orders")
    print("2. Add New Customer Order")
    print("3. Exit")
 
def main():
    menu_items, book_list, customer_data, customer_list = load_data()
    customer_number = len(customer_list)  # Keeps track of customer entries
    while True:
        display_main_menu()
        user_choice = input("Enter your choice: ")
        if user_choice == "1":  # Customer
            while True:
                customer_menu()
                customer_choice = input("Enter your choice: ")
                if customer_choice == "1":
                    print("Food and Drinks:", menu_items)
                    print("Books:", book_list)
                elif customer_choice == "2":
                    food_and_drink_choices = input("Choose food and drinks: ")
                    book_choices = input("Choose books: ")
                    customer_details = input("Enter your details: ")
                    new_order = {"customer": customer_details, "food": food_and_drink_choices, "books": book_choices}
                    customer_data.append(new_order)
                    save_json(data_files["customers"], customer_data)
                    print("Order Confirmed!")
                elif customer_choice == "3":
                    break
                else:
                    print("Invalid choice.")
        elif user_choice == "2":  # Employee
            while True:
                employee_menu()
                employee_choice = input("Enter your choice: ")
                if employee_choice == "1":
                    print("Update Menu and Books")
                elif employee_choice == "2":
                    print("Update Specials")
                elif employee_choice == "3":
                    print("View Orders")
                    print(json.dumps(customer_data, indent=4))
                elif employee_choice == "4":
                    break
                else:
                    print("Invalid choice.")
        elif user_choice == "3":  # Delivery System
            DeliveryService.DeliveryStart()
        elif user_choice == "4":  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
if __name__ == "__main__":
    main()