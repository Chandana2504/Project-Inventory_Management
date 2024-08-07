class Inventory:
    def __init__(self):
        """Initialize the inventory with an empty dictionary to store products"""
        self.products = {}

    def add_product(self, product):
        """Add a new product to the inventory, product: Product object to add
        """
        self.products[product.product_id] = product

    def update_product(self, product_id, **kwargs):
        """Update the details of an existing product
           product_id: ID of the product to update
           kwargs: Fields to update (e.g. price, quantity) """
        
        if product_id in self.products:
            product = self.products[product_id]
            if 'price' in kwargs:
                product.update_price(kwargs['price'])
            if 'quantity' in kwargs:
                product.update_quantity(kwargs['quantity'])

    def remove_product(self, product_id):
        """Remove a product from the inventory, product_id: ID of the product to remove"""
        if product_id in self.products:
            del self.products[product_id]

    def view_all_products(self):
        """View all products in the inventory, return: List of products with their details"""
        return list(self.products.values())
