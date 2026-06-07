# =============================================
# PAYMENT SYSTEM
# =============================================

class PaymentMethod:

    def __init__(self, amount, transaction_id, payment_status = "Pending"):
        self.amount = amount
        self.transaction_id = transaction_id
        self.payment_status = payment_status

    def process_payment(self):
        self.payment_status = "Processed"
        print("\n=============== PAYMENT DETAILS ===============")
        print("Amount:", self.amount)
        print("Transaction ID:", self.transaction_id)
        print("Payment Status:", self.payment_status)

class UPIPayment(PaymentMethod):

    def __init__(self, amount, transaction_id, payment_status = "Pending", upi_id = ""):
        super().__init__(amount, transaction_id, payment_status)
        self.upi_id = upi_id

    def verify_upi_id(self):
        if "@" in self.upi_id:
            print("UPI ID", self.upi_id, "is valid.")
        else:
            print("Invalid UPI ID. Please enter a valid UPI ID.")

class CardPayment(PaymentMethod):

    def __init__(self, amount, transaction_id, payment_status = "Pending", card_number = ""):
        super().__init__(amount, transaction_id, payment_status)
        self.card_number = card_number

    def verify_card_number(self):
        if len(self.card_number) == 16 and self.card_number.isdigit():
            print("Card number", self.card_number, "is valid.")
        else:
            print("Invalid card number. Please enter a valid 16-digit card number.")

class WalletPayment(PaymentMethod):

    def __init__(self, amount, transaction_id, payment_status = "Pending", wallet_balance = ""):
        super().__init__(amount, transaction_id, payment_status)
        self.wallet_balance = wallet_balance

    def check_wallet_balance(self):
        if self.wallet_balance >= self.amount:
            print("Wallet balance is sufficient.")
        else:
            print("Insufficient wallet balance.")

class EMIPayment(PaymentMethod):

    def __init__(self, amount, transaction_id, payment_status = "Pending", emi_months = 0):
        super().__init__(amount, transaction_id, payment_status)
        self.emi_months = emi_months

    def calculate_emi(self):
        if self.emi_months > 0:
            emi_amount = self.amount / self.emi_months
            print("EMI Amount for", self.emi_months, "months is:", round(emi_amount, 2))
        else:
            print("Please enter a valid number of EMI months.")

Upi = UPIPayment(1000, "TXN12345", upi_id = "user@bank")

Upi.process_payment()
Upi.verify_upi_id()

Card = CardPayment(1000, "TXN12346", card_number = "1234567890123456")

Card.process_payment()
Card.verify_card_number()

Wallet = WalletPayment(1000, "TXN12347", wallet_balance = 1500)

Wallet.process_payment()
Wallet.check_wallet_balance()

Emi = EMIPayment(1000, "TXN12348", emi_months = 12)

Emi.process_payment()
Emi.calculate_emi()
