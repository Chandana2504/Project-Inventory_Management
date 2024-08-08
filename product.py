class Product:
    def __init__(self, product_id, name, category, price, quantity):
        """Initializing a new product and parameter represents, 
           product_id:Unique identifier for the product
           name:Name of product
           category: the prodcut belongs to which category
           price: Price of the product
           quantity: Quantity of the product available in inventory"""
        
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        """Update the quantity of the product, quantity:New quantity to set"""
        
        self.quantity = quantity

    def update_price(self, price):
        """Update the price of the product, price: New price to set"""
        self.price = price
        
