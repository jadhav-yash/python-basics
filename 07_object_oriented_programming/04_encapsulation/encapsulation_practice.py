# ==========================================
# ENCAPSULATION
# ==========================================

class BankAccount:

    # ======================================
    # CONSTRUCTOR
    # ======================================

    def __init__(self, name, balance):

        # Public Variable
        self.name = name

        # Private Variable
        self.__balance = balance


    # ======================================
    # DEPOSIT METHOD
    # ======================================

    def deposit(self, amount):

        self.__balance += amount

        print(f"₹{amount} Deposited Successfully")


    # ======================================
    # WITHDRAW METHOD
    # ======================================

    def withdraw(self, amount):

        # Check sufficient balance
        if amount <= self.__balance:

            self.__balance -= amount

            print(f"₹{amount} Withdrawn Successfully")

        else:

            print("Insufficient Balance")


    # ======================================
    # SHOW BALANCE METHOD
    # ======================================

    def show_balance(self):

        print(f"Current Balance = ₹{self.__balance}")


# ==========================================
# OBJECT CREATION
# ==========================================

user1 = BankAccount("Rahul", 10000)

# ==========================================
# ACCESS PUBLIC VARIABLE
# ==========================================

print("Account Holder:", user1.name)

# ==========================================
# CALL METHODS
# ==========================================

user1.deposit(5000)

user1.withdraw(3000)

user1.show_balance()