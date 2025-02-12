import json

#Initialising a few variables at first. "deliveryMode" is essentially a "while true".
#Keeps track of where the json is.
customerList = r'customer_list.json'
#"customerNumber" keeps track of the new nested dictionaries for new customers that need to be initialised. every nested dictionary needs it's own number. 
# I'm starting this with an example json with 2 customers already there.
customerNumber = 2

#A quick function that views all active orders.
def ViewDeliveries():
    with open (customerList, 'r') as json_file:
        loaded_data = json.load(json_file)
    print(json.dumps(loaded_data, indent=4))

#This delivery function allows the user total control, like entering a custom order into the database.
def DeliveryStart():
    #This function has the deliveryMode act a bit like a 'while True' system.
    deliveryMode = True
    while deliveryMode == True:
        userInput = input("\nWelcome to the delivery system!\nType 'Quit' to go back.\nType 'View All' to view all active orders.\nType 'Add' to add a new customer.")
        if userInput.lower() == 'quit':
            deliveryMode = False
        elif userInput.lower() == 'view all':
            ViewDeliveries()
        elif userInput.lower() == 'add':
                #Makes a new customer dictionary based on user input.
                global customerNumber
                customerNumber += 1
                newCustomerAlias = "customer"+(str(customerNumber))
                newCustomerName = input("\nOk, what's this customer's name?")
                newCustomerOrder = input("\nOk, what's this customer ordered?")
                newCustomerAddress = input("\nOk, where does this customer live?")
                newCustomerDetails = {
                    newCustomerAlias:{
                        "name":newCustomerName,
                        "order":newCustomerOrder,
                        "location":newCustomerAddress
                    }
                }
                #Gets the customer dict from json
                with open(customerList, 'r') as json_file:
                    existingCustomerList = json.load(json_file)
                #Merges the existing customer dict, with the new customer dict 
                existingCustomerList = existingCustomerList | newCustomerDetails
                
                #Overwrites the previous customer dict with the newest version
                with open (customerList, 'w') as json_file:
                    json.dump(existingCustomerList,json_file)
        else:
            print("I don't recognise that command, sorry. Try again!\n")

#This function is a condensed version of the one above and is designed to be customer-facing, instead of employee facing.
def PlaceBookOrder():
     #Makes a new customer dictionary based on user input.
        global customerNumber
        customerNumber += 1
        newCustomerAlias = "customer"+(str(customerNumber))
        newCustomerName = input("\nPlease enter your name!")
        newCustomerOrder = input("\nPlease enter the book you'd like to order!")
        newCustomerAddress = input("\nPlease enter your full address!")
        newCustomerDetails = {
            newCustomerAlias:{
                "name":newCustomerName,
                "order":newCustomerOrder,
                "location":newCustomerAddress
            }
        }
        
        #Gets the customer input from json
        with open(customerList, 'r') as json_file:
            existingCustomerList = json.load(json_file)
        #Merges the existing customer dict with the new customer dict 
        existingCustomerList = existingCustomerList | newCustomerDetails
                
        #Overwrites the previous customer dict with the newest version
        with open (customerList, 'w') as json_file:
            json.dump(existingCustomerList,json_file)


#This function is even more condensed and designed to be entirely backend, giving the user no visible output. It also takes in the necessary stuff for the order as parameters.
def QuickOrder(name, order, address):
     #Makes a new customer dictionary based on user input.
        global customerNumber
        customerNumber += 1
        newCustomerAlias = "customer"+(str(customerNumber))
        newCustomerName = name
        newCustomerOrder = order
        newCustomerAddress = address
        newCustomerDetails = {
            newCustomerAlias:{
                "name":newCustomerName,
                "order":newCustomerOrder,
                "location":newCustomerAddress
            }
        }
        #Gets the customer input from json
        with open(customerList, 'r') as json_file:
            existingCustomerList = json.load(json_file)
        #Merges the existing customer dict with the new customer dict 
        existingCustomerList = existingCustomerList | newCustomerDetails
                
        #Overwrites the previous customer dict with the newest version
        with open (customerList, 'w') as json_file:
            json.dump(existingCustomerList,json_file)

