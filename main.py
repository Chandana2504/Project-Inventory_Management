from inventory import Inventory
from product import Product
from invoice import Invoice
from datetime import datetime

def main():
    inventory = Inventory()

    while True:
        print("\n1. Add Product")
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
            print('Product added successfully')
        
        elif choice == '2':
            product_id = input("Enter product ID: ")
            price = float(input("Enter new product price (or 0 to skip): "))
            quantity = int(input("Enter new product quantity (or -1 to skip): "))
            kwargs = {}
            if price > 0:
                kwargs['price'] = price
            if quantity >= 0:
                kwargs['quantity'] = quantity
            inventory.update_product(product_id, **kwargs)
            print("Product updated successfully.",inventory.products)
        
        elif choice == '3':
            product_id = input("Enter product ID to remove: ")
            inventory.remove_product(product_id)
            print("Product removed successfully.")
        
        elif choice == '4':
            products = inventory.view_all_products()
            for product in products:
                print(f"ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: {product.price}, Quantity: {product.quantity}")
        
        elif choice == '5':
            transaction_id = input("Enter transaction ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity sold: "))
            sale_price = float(input("Enter sale price: "))
            date = datetime.now().strftime("%Y-%m-%d")
            inventory.record_sale(transaction_id, product_id, quantity, sale_price, date)
            print("Sale recorded successfully.")
        
        elif choice == '6':
            transaction_id = input("Enter transaction ID: ")
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity returned: "))
            reason = input("Enter return reason: ")
            date = datetime.now().strftime("%Y-%m-%d")
            inventory.record_return(transaction_id, product_id, quantity, reason, date)
            print("Return recorded successfully.")
        
        elif choice == '7':
            invoice_id = input("Enter invoice ID: ")
            transactions = inventory.transactions
            invoice = Invoice(invoice_id, transactions)
            filename = input("Enter filename for invoice: ")
            invoice.generate_pdf(filename)
            print("Invoice generated successfully.")
        
        elif choice == '8':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

