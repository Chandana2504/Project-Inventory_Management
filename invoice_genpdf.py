import fpdf

class Invoice:
    def __init__(self, invoice_id, transactions):
        """Initialize a new invoice, Parameters description: 
           invoice_id: Unique identifier for the invoice
           transactions: List of transactions to include in the invoice """
        self.invoice_id = invoice_id
        self.transactions = transactions

    def generate_pdf(self, filename):
        """Generate a PDF file for the invoice.
           filename: Name of the PDF file to save """
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Header
        pdf.cell(200, 10, txt="Invoice", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Invoice ID: {self.invoice_id}", ln=True, align='L')

        # Transaction details
        for transaction in self.transactions:
            pdf.cell(200, 10, txt=f"Transaction ID: {transaction.transaction_id}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Product ID: {transaction.product_id}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Quantity: {transaction.quantity}", ln=True, align='L')
            pdf.cell(200, 10, txt=f"Date: {transaction.date}", ln=True, align='L')
            if isinstance(transaction, Sale):
                pdf.cell(200, 10, txt=f"Sale Price: {transaction.sale_price}", ln=True, align='L')
            elif isinstance(transaction, Returns):
                pdf.cell(200, 10, txt=f"Reason: {transaction.reason}", ln=True, align='L')
            pdf.cell(200, 10, txt=" ", ln=True, align='L')  # Blank line

        pdf.output(filename)