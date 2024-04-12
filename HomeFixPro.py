import uuid

## DB
admin = {"username": "admin1", "password": 1234}
users = {"user": "123"}
user_session = {}  # User session dictionary to store session IDs
quantity=0
# Function to generate a session ID
def generate_session_id():
    return str(uuid.uuid4())


category = {
    "1":"Maintenance",
    "2":"Plumbing",
    "3":"Electrical",
    "4": "Painting"
}

catalog = {
    "1": {"service name": "Routine maintenance checks", "category_id": "1", "price": 100,"workers":10},
    "2": {"service name": "Ceep cleaning servicese", "category_id": "1", "price": 100,"workers":10},
    "3": {"service name": "lawn care and landscaping maintenance service", "category_id": "1", "price": 100,"workers":10},
    "4": {"service name": "Drain cleaning services", "category_id": "2", "price": 200, "workers":12},
    "5": {"service name": "Leak detection and repair services", "category_id": "2", "price": 200, "workers":12},
    "6": {"service name": "Pipe repair or replacement services", "category_id": "2", "price": 200, "workers":12},
    "7": {"service name": "Electrical wiring installation or upgrades", "category_id": "3", "price": 150, "workers":10},
    "8": {"service name": "Troubleshooting and repair services", "category_id": "3", "price": 150, "workers":10},
    "9": {"service name": "Electrical panel upgrades or replacements", "category_id": "3", "price": 150, "workers":10},
    "10": {"service name": "Interior Painting services", "category_id": "4", "price": 50, "workers":12},
    "11": {"service name": "Exterior Painting services", "category_id": "4", "price": 50, "workers":12},
    "12": {"service name": "Drywall repair and texturing services", "category_id": "4", "price": 50, "workers":12},
}




days = {
    "Maintenance": ["Sunday", "Monday", "Tuesday", "Wednsday","Thursday"],
    "Plumbing": ["Sunday", "Monday", "Tuesday", "Wednsday","Thursday"],
    "Electrical": ["Sunday", "Monday", "Tuesday", "Wednsday","Thursday"],
    "Painting": ["Sunday", "Monday", "Tuesday", "Wednsday","Thursday"]
}

def adminMenu():
    print("*********************")
    print("1. Display Menu")
    print("2. Add Category")
    print("3. Add Service")
    print("4. Remove Category")
    print("5. Logout")
    print("*********************")


def DisplayMenu():
    print("Category ID\tCategory Name")
    for category_id, category_name in category.items():
        print(f"{category_id}\t\t{category_name}")
    
    category_choice = input("Choose a category ID: ")
    
    if category_choice in catalog:
        print("\nProduct ID\tService Name\t\tPrice\tAvailable workers")
        for product_id, product in catalog.items():
            if product["category_id"] == str(category_choice):
                productID = product_id
                service_name = product["service name"]
                price = product["price"]
                workers = product["workers"]
                print(f"{productID}\t\t{service_name}\t\t${price}\t{workers}")
    else:
        print("Invalid category ID.")


def DisplayAvailableDays(category_id):
    if category_id in category:
        category_name = category[category_id]
        if category_name in days:
            available_days = days[category_name]
            print("\nAvailable days for {}:\n {}".format(category_name, ',\t '.join(available_days)))
            
            chosen_day = input("Choose a suitable day for your service: ")
            if chosen_day in available_days:
                available_days.remove(chosen_day)
                print(f"{chosen_day} has been chosen.")
            else:
                print("Invalid day choice.")
        else:
            print("No days available for this category.")
    else:
        print("Invalid Category ID.")
  


def addItem():
    new_category_name = input("Enter the new category name: ")
    category_id = str(len(category) + 1)

    # Add the new category to the category dictionary
    category[category_id] = new_category_name

    print(f"Category '{new_category_name}' added successfully with ID '{category_id}'.")

    # Ask if the admin wants to add services to the newly added category
    add_service = input("Do you want to add services to this category? (yes/no): ")
    if add_service.lower() == "yes":
        addService(category_id)


def addService(category_id):
    while True:
        service_name = input("Enter the service name: ")
        price = input("Enter the price of the service: $")
        workers = input("Enter the number of available workers for this service: ")

        # Generate a new ID for the service
        new_id = str(len(catalog) + 1)

        # Add the new service to the catalog dictionary
        catalog[new_id] = {"service name": service_name, "category_id": category_id, "price": price, "workers": workers}

        print(f"Service '{service_name}' added successfully with ID '{new_id}' to category '{category[category_id]}'.")

        add_more = input("Do you want to add more services to this category? (yes/no): ")
        if add_more.lower() != "yes":
            break


def removeItem():
    remove_category_id = input("Enter the ID of the category to remove: ")

    if remove_category_id in category:
        del category[remove_category_id]

        # Remove services associated with the removed category from the catalog
        for service_id in list(catalog.keys()):
            if catalog[service_id]["category_id"] == remove_category_id:
                del catalog[service_id]

        print(f"Category with ID '{remove_category_id}' removed successfully.")
    else:
        print("Invalid category ID. Please enter a valid ID.")




def admin_login():
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    if admin['username'] == username and admin['password'] == int(password):
        print("Admin login successful!")
        adminMenu()
    else:
        print("Invalid username or password for admin.")
        login()


def adminChoice():
    choice = int(input("\nPlease enter your choice : "))
    if choice == 1:
        DisplayMenu()
        print("\n***************************************************\n")
        adminMenu()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 2:
        addItem()
        print("\n***************************************************\n")
        adminMenu()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 3:
        addService()
        print("\n***************************************************\n")
        adminMenu()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 4:
        removeItem()
        print("\n***************************************************\n")
        adminMenu()
        print("\n***************************************************\n")
        adminChoice()
    elif choice == 5:
        logout()
    else:
        print("\nInvalid Choice. Please enter valid choice")
        print("\n***************************************************\n")
        adminMenu()
        print("\n***************************************************\n")
        adminChoice()

def user_login():
    print("1. Login")
    print("2. Sign up")
    choice = input("Enter your choice: ")

    if choice == '1':
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            session_id = generate_session_id()
            user_session[session_id] = username
            print("User login successful. Session ID:", session_id)
            userMenu()
            userChoice(session_id)  # Pass session_id to userChoice
        else:
            print("User does not exist. Please try again.")
            user_login()
    elif choice == '2':
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        if username not in users:
            users[username] = password
            session_id = generate_session_id()
            user_session[session_id] = username
            print("User signed up successfully!")
            user_login()
        else:
            print("Username already exists!!")
            user_login()
    else:
        print("Invalid choice.")


def place_order(session_id, category):
    print("The Categories:")
    for i, category_id in enumerate(category.keys()):
        print(f"{i + 1}. {category[category_id]}")
    
    category_choice = input("\nFirstly, choose from the available categories: ")
    category_choice = int(category_choice)

    if category_choice in range(1, len(category) + 1):
        category_list = list(category.keys())
        chosen_category = category_list[category_choice - 1]

        print("\nAvailable Services for", category[chosen_category], ":")
        print("\nProduct ID\tService Name\t\tPrice\tAvailable workers")
        for product_id, product in catalog.items():
            if product["category_id"] == str(category_choice):
                productID = product_id
                service_name = product["service name"]
                price = product["price"]
                workers = product["workers"]
                print(f"{productID}\t\t{service_name}\t\t${price}\t{workers}")
        
        service_choice = input("Secondly, choose from the available services: ")
        service_choice = int(service_choice)

        if service_choice in range(1, len(catalog) + 1):
            chosen_service_id = str(service_choice)
            chosen_service_name = catalog[chosen_service_id]['service name']
            quantity = int(input("How many workers (quantity) you need? "))
            add_to_cart(session_id, chosen_service_name, quantity)
            DisplayAvailableDays(chosen_category)
        else:
            print("Invalid service choice.")
    else:
        print("Invalid category choice.")




def add_to_cart(session_id, chosen_service, quantity):
    if session_id in user_session:
        # Check if service exists and quantity is valid
        found = False
        for product_id, product in catalog.items():
            if product['service name'] == chosen_service and quantity > 0:
                # Reduce the available workers for the chosen service
                product["workers"] -= quantity
                found = True
                break
        
        if found:
            print("Service added to cart.")
        else:
            print("Invalid service or quantity.")
    else:
        print("Invalid session ID.")


def remove_from_cart(session_id, chosen_service, quantity):
    if session_id in user_session:
        # Check if product exists and quantity is valid
        if chosen_service in catalog and quantity > 0:
            # Increase the available workers for the chosen service
            catalog[chosen_service]["workers"] += quantity
            print("Service removed from cart.")
        else:
            print("Invalid service ID or quantity.")
    else:
        print("Invalid session ID.")


def checkout(session_id, payment_option):
    if session_id in user_session:
            user_cart = {}
            total_amount = 0
            for product_id, product in catalog.items():
                if product["workers"] < 10:
                    user_cart[product["service name"]] = product["workers"]
                    total_amount += product["price"]
            
            if not user_cart:
                print("Your cart is empty.")
                return
            
            # Generate and display the invoice or order summary
            print("---------- Invoice ----------")
            print("Service Name\tQuantity\tPrice")
            for service, quantity in user_cart.items():
                found = False
                for catalog_service in catalog.values():
                    if service == catalog_service["service name"]:
                        price = catalog_service["price"]
                        print(f"{service}\t\t{quantity}\t\t${price}")
                        found = True
                        
                if not found:
                    print(f"{service} not found in catalog.")
            print("-----------------------------")
            print(f"Total Amount: ${total_amount}")
            print("this is only the initial invoice of your cart, the total price will be changed after the workers visit you")
            
            # Save invoice to file
            invoice_filename = f"Invoice_{session_id}.txt"
            with open(invoice_filename, 'w') as invoice_file:
                invoice_file.write("---------- Invoice ----------\n")
                invoice_file.write("Service Name\tQuantity\tPrice\n")
                for service, quantity in user_cart.items():
                    found = False
                    for catalog_service in catalog.values():
                        if service.strip().lower() == catalog_service["service name"].strip().lower():
                            price = catalog_service["price"]
                            invoice_file.write(f"{service}\t\t{quantity}\t\t${price}\n")
                            found = True

                    if not found:
                        invoice_file.write(f"{service} not found in catalog.\n")
                invoice_file.write("-----------------------------\n")
                invoice_file.write(f"Total Amount: ${total_amount}\n")
                invoice_file.write("this is only the initial invoice of your cart, the total price will be changed after the workers visit you\n")
            
            # Process payment
            if payment_option == "UPI" or payment_option == "1":
                print("\nYou will be shortly redirected to the portal for Unified Payment Interface.")
            elif payment_option == "Debit Card" or payment_option == "2":
                print("\nPlease enter your debit card details.")
                cardno = input("Card Number: ")
                cardcuv = input("Card Password (CUV): ")
            else:
                print("Invalid payment option.")

            print("Your order is successfully placed. Invoice saved to:", invoice_filename)
    else:
            print("Invalid session ID.")



def logout():
    print("Thank you for visiting FixHomePro!!\n")
    login()
    #exit()

def user_logout():
    print("Thank you for purchasing from FixHomePro, Visit us again!!\n")
    #login()
    exit()


def userMenu():
    print("__________________________\n")
    print("1. Display Menu")
    print("2. Add Services to your cart")
    print("3. Remove Services from your cart")
    print("4. Checkout")
    print("5. Logout")
    print("\n__________________________")


def userChoice(session_id): 
    choice = input("\nPlease enter your choice: ")
    if choice == '1':
        DisplayMenu()
        print("\n___________________________________________________\n")
        userChoice(session_id) 
    elif choice == '2':
        place_order(session_id, category)
        userChoice(session_id) 
        print("\n___________________________________________________\n")
        user_login()
    elif choice == '3':
        product_id = input("Enter the Service ID you want to remove: ")
        quantity = int(input("How many workers (quantity) you want to remove: "))
        remove_from_cart(session_id, product_id, quantity)
        userChoice(session_id) 
        print("\n___________________________________________________\n")
    elif choice == '4':
        payment_option = input("Enter the payment option (1 for UPI, 2 for Debit Card): ")
        checkout(session_id, payment_option) 
        userChoice(session_id)  
        print("\n___________________________________________________\n")
    elif choice == '5':
        user_logout()
    else:
        print("Invalid Choice. Please enter a valid choice")


def login():
    tp = input("Login as Admin or as User [A/U] : ")
    if tp == 'A' or tp == 'a':
        admin_login()
        adminChoice()

    elif tp == 'U' or tp == 'u':
        user_login()
    else:
        print("Invalid choice. Enter a valid choice")


print("-----------------------------------------")
print("         WELCOME TO HomeFixPro           ")
print("-----------------------------------------")
login()
