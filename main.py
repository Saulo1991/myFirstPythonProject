store_products = ["car", "shirt", "skirt", "laptop", "suit"]

def add_product(store_products_add):
    request = input("Type a product that you wish to add to the list: ").lower()
    
    store_products_add.append(request)
    print(f"New product added: {request}")

def remove_products(store_products_rm):
    request = input("Type a product you wish to remove: ").lower()
    
    if request in store_products_rm:
        store_products_rm.remove(request)
    else:
        print(f"Product {request} not found in the list")
        
    print(f"Product removed! Updated list: {store_products_rm}")

def listing_products(store_products_listing):
    for product in store_products_listing:
        print(f"Product: {product}")

while True:
    option = input("Which option do you wish?\n(1) Add product\n(2) Remove product\n(3) List products\nPress 0 to exit: ")
    print('')
    print('')
    
    if option == "1":
        add_product(store_products)
    
    elif option == "2":
        remove_products(store_products)
        
    elif option == "3":
        listing_products(store_products)
    
    elif option == "0":
        print("You left the page")
        break
    else:
        print("Invalid option")