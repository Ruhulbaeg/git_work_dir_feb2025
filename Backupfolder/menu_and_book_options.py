# The employee picked option 1 'Update menu and Books'
'''I need the dictionary files to call to be able to test'''
import json

menu = r"D:/AWS Restart files/Cafe Book Project/menu_placeholder.json"
books = r"D:/AWS Restart files/Cafe Book Project/books_placeholder.json"


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
    
    choice = int(input("""Do you want to (1) add/update an item or (2) 
                       remove an item or (3) exit: (1, 2, or 3):  """))
    if choice in [1, 2, 3]:
        if choice == 1:
            key = input("What would you like to change or add?:  ")
            value = input("Enter the change or new value: ")
            data[key] = value
        elif choice == 2:
            key = input("key: ")
            data.pop(key, None)
        elif choice == 3:
            employee_options()
            return
    else:
        print("Invalid choice")
    
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

# Go back to the employee options

employee_options()

'''The other main options pages will look similar to this I just need to
be sure I'm calling the dictionaries correctly, then tomorrow I can add:
- Update specials
- Update customer info
- View current orders
- Exit'''