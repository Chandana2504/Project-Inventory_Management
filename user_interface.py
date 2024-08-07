import datetime

def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. View All Products")
        print("5. Record Sale")
        print("6. Record Return")
        print("7. Generate Invoice")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, category, price, quantity)
            inventory.add_product(product)
            print("Product added successfully.")

        elif choice == "2":
            product_id = input("Enter product ID to update: ")
            name = input("Enter product name: ")
            category = input("Enter product category: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, category, price, quantity)
            inventory.update_product(product)
            print("Product updated successfully.")
        else:   
            print("invalid choice,try again! ") 