# ============================================================
# BANKING SYSTEM USING INHERITANCE
# ============================================================

# ============================================================
# PARENT CLASS
# ============================================================

class BankAccount:

    """
    Parent Class

    This class contains common features
    shared by all bank accounts.
    """

    # ========================================================
    # CONSTRUCTOR
    # ========================================================

    def __init__(self, account_holder, balance):

        # Store account holder name
        self.account_holder = account_holder

        # Store account balance
        self.balance = balance

    # ========================================================
    # COMMON METHOD
    # ========================================================

    def show_balance(self):

        # Display account details
        print("\nAccount Holder:", self.account_holder)

        print("Current Balance:", self.balance)

    # ========================================================
    # DEPOSIT METHOD
    # ========================================================

    def deposit(self, amount):

        # Add money to account balance
        self.balance += amount

        print(amount, "Deposited Successfully")

    # ========================================================
    # WITHDRAW METHOD
    # ========================================================

    def withdraw(self, amount):

        # Check if balance is enough
        if amount <= self.balance:

            # Deduct money
            self.balance -= amount

            print(amount, "Withdraw Successful")

        else:

            print("Insufficient Balance")

# ============================================================
# CHILD CLASS 1
# ============================================================

class SavingsAccount(BankAccount):

    """
    Savings Account Child Class

    Inherits all features from BankAccount
    """

    # ========================================================
    # SPECIAL METHOD
    # ========================================================

    def add_interest(self):

        # Add interest to balance
        interest = self.balance * 0.05

        self.balance += interest

        print("5% Interest Added")

# ============================================================
# CHILD CLASS 2
# ============================================================

class CurrentAccount(BankAccount):

    """
    Current Account Child Class

    Inherits all common features
    """

    # ========================================================
    # SPECIAL METHOD
    # ========================================================

    def business_loan(self):

        print("Business Loan Approved")

# ============================================================
# CHILD CLASS 3
# ============================================================

class SalaryAccount(BankAccount):

    """
    Salary Account Child Class
    """

    # ========================================================
    # SPECIAL METHOD
    # ========================================================

    def salary_credit(self):

        print("Monthly Salary Credited")

# ============================================================
# OBJECT CREATION
# ============================================================

# Creating Savings Account object
saving_user = SavingsAccount("Harsh", 10000)

# Creating Current Account object
current_user = CurrentAccount("Rahul", 50000)

# Creating Salary Account object
salary_user = SalaryAccount("Priya", 30000)

# ============================================================
# SAVINGS ACCOUNT OPERATIONS
# ============================================================

saving_user.show_balance()

saving_user.deposit(2000)

saving_user.withdraw(3000)

saving_user.add_interest()

saving_user.show_balance()

# ============================================================
# CURRENT ACCOUNT OPERATIONS
# ============================================================

current_user.show_balance()

current_user.business_loan()

current_user.withdraw(10000)

current_user.show_balance()

# ============================================================
# SALARY ACCOUNT OPERATIONS
# ============================================================

salary_user.show_balance()

salary_user.salary_credit()

salary_user.deposit(15000)

salary_user.show_balance()