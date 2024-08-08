from product import Product
from inventory import Inventory
from invoice import Invoice
from datetime import datetime

def run_test():
    # Initialize the inventory
    inventory = Inventory()

    # Add products
    product1 = Product(product_id="P001", name="Laptop", category="Electronics", price=1000.00, quantity=10)
    product2 = Product(product_id="P002", name="Smartphone", category="Electronics", price=500.00, quantity=20)
    inventory.add_product(product1)
    inventory.add_product(product2)
    print("Products added successfully.")

    # Record a sale
    transaction_id1 = "T001"
    quantity_sold1 = 2
    sale_price1 = 950.00
    date1 = datetime.now().strftime("%Y-%m-%d")
    inventory.record_sale(transaction_id1, product1.product_id, quantity_sold1, sale_price1, date1)
    print("Sale recorded successfully.")

    # Record another sale
    transaction_id2 = "T002"
    quantity_sold2 = 3
    sale_price2 = 450.00
    date2 = datetime.now().strftime("%Y-%m-%d")
    inventory.record_sale(transaction_id2, product2.product_id, quantity_sold2, sale_price2, date2)
    print("Another sale recorded successfully.")

    # Generate an invoice
    invoice_id = "INV001"
    transactions = inventory.transactions
    invoice = Invoice(invoice_id, transactions)
    filename = "invoice_test.pdf"
    invoice.generate_pdf(filename)
    print("Invoice generated successfully as", filename)

if __name__ == "_main_":
    run_test()
