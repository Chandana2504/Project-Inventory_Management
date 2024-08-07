class Inventory:
    def __init__(self):
        self.products = {}
        self.transactions = []

    def add_product(self, product):
        self.products[product.product_id] = product

    def update_product(self, product_id, **kwargs):
        if product_id in self.products:
            product = self.products[product_id]
            if 'price' in kwargs:
                product.update_price(kwargs['price'])
            if 'quantity' in kwargs:
                product.update_quantity(kwargs['quantity'])

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def view_all_products(self):
        return list(self.products.values())

    def record_sale(self, transaction_id, product_id, quantity, sale_price, date):
        """Record a sale transaction and update inventory.
           transaction_id: Unique identifier for the sale
           product_id: ID of the product sold
           quantity: Quantity of the product sold
           sale_price: Sale price of the product
           date: Date of the sale """
        if product_id in self.products and self.products[product_id].quantity >= quantity:
            sale = Sale(transaction_id, product_id, quantity, sale_price, date)
            self.transactions.append(sale)
            self.products[product_id].quantity -= quantity

    def record_return(self, transaction_id, product_id, quantity, reason, date):
        """Record a return transaction and update inventory.
           transaction_id: Unique identifier for the return
           product_id: ID of the product returned
           quantity: Quantity of the product returned
           reason: Reason for the return
           date: Date of the return """
        if product_id in self.products:
            return_transaction = Returns(transaction_id, product_id, quantity, reason, date)
            self.transactions.append(return_transaction)
            self.products[product_id].quantity += quantity 