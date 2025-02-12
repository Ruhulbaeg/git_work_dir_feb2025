import json

customerList = r'customer_list.json'

def customer_menu_options():
    options = input("""Would you like to view a list of customers or exit?\n
                    1. View customer list\n
                    2. Exit\n
                    Enter your choice: """)
    if options.lower() == "view customer list" or options =="1":
        print("Here is the list of current customers and their order")
        with open (customerList, 'r') as json_file:
            loaded_data = json.load(json_file)
            print(json.dumps(loaded_data, indent=4))  # Pretty print the JSON data
    elif options.lower() == "exit" or options == "2":
         return
    else:
         input("Please enter a valid choice: ")


customer_menu_options()
