class Transaction:
    def __init__(self, transaction_id, product_id, quantity, date):
        """
        Initialize a new transaction, parameters description:
        transaction_id: Unique identifier for the transaction
        product_id: ID of the product involved in the transaction
        quantity: Quantity of the product in the transaction
        date: Date of the transaction """

        self.transaction_id = transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.date = date

class Sale(Transaction):
    def __init__(self, transaction_id, product_id, quantity, sale_price, date):
        """Initialize a new sale transaction, Parameters description:
           transaction_id: Unique identifier for the sale
           product_id: ID of the product sold
           quantity: Quantity of the product sold
           sale_price: Sale price of the product
           date: Date of the sale """
        super().__init__(transaction_id, product_id, quantity, date)
        self.sale_price = sale_price

class Returns(Transaction):
    def __init__(self, transaction_id, product_id, quantity, reason, date):
        """Initialize a new return transaction,parameters description:
           transaction_id: Unique identifier for the return
           product_id: ID of the product returned
           quantity: Quantity of the product returned
           reason: Reason for the return
           date: Date of the return """
        super().__init__(transaction_id, product_id, quantity, date)
        self.reason = reason
        
