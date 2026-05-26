# ============================================================
# ATM MACHINE SYSTEM
# ============================================================

# Default ATM PIN
correct_pin = 1234

# Default account balance
balance = 50000

# ============================================================
# USER INPUT
# ============================================================

print("=========== WELCOME TO ATM ===========")

entered_pin = int(input("Enter Your 4 Digit PIN: "))

# ============================================================
# PIN CHECK USING IF ELSE
# ============================================================

if entered_pin == correct_pin:

    print("PIN Verified Successfully")

    # --------------------------------------------------------
    # MENU OPTIONS
    # --------------------------------------------------------

    print("\n=========== ATM MENU ===========")

    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Fast Cash")
    print("5. Change PIN")

    choice = int(input("Enter Your Choice: "))

    # ========================================================
    # OPTION 1 - CHECK BALANCE
    # ========================================================

    if choice == 1:

        print("\n=========== BALANCE CHECK ===========")

        print("Available Balance:", balance)

    # ========================================================
    # OPTION 2 - DEPOSIT MONEY
    # ========================================================

    elif choice == 2:

        print("\n=========== DEPOSIT MONEY ===========")

        deposit_amount = int(input("Enter Deposit Amount: "))

        if deposit_amount > 0:

            balance = balance + deposit_amount

            print("Money Deposited Successfully")

            print("Updated Balance:", balance)

        else:

            print("Invalid Deposit Amount")

    # ========================================================
    # OPTION 3 - WITHDRAW MONEY
    # ========================================================

    elif choice == 3:

        print("\n=========== WITHDRAW MONEY ===========")

        withdraw_amount = int(input("Enter Withdraw Amount: "))

        if withdraw_amount <= balance:

            if withdraw_amount > 0:

                balance = balance - withdraw_amount

                print("Please Collect Your Cash")

                print("Remaining Balance:", balance)

            else:

                print("Invalid Withdraw Amount")

        else:

            print("Insufficient Balance")

    # ========================================================
    # OPTION 4 - FAST CASH
    # ========================================================

    elif choice == 4:

        print("\n=========== FAST CASH ===========")

        print("1. 500")
        print("2. 1000")
        print("3. 2000")
        print("4. 5000")

        fast_cash_choice = int(input("Select Fast Cash Option: "))

        if fast_cash_choice == 1:

            amount = 500

        elif fast_cash_choice == 2:

            amount = 1000

        elif fast_cash_choice == 3:

            amount = 2000

        elif fast_cash_choice == 4:

            amount = 5000

        else:

            amount = 0

            print("Invalid Option")

        if amount > 0:

            if amount <= balance:

                balance = balance - amount

                print("Please Collect Cash:", amount)

                print("Remaining Balance:", balance)

            else:

                print("Insufficient Balance")

    # ========================================================
    # OPTION 5 - CHANGE PIN
    # ========================================================

    elif choice == 5:

        print("\n=========== CHANGE PIN ===========")

        old_pin = int(input("Enter Old PIN: "))

        if old_pin == correct_pin:

            new_pin = int(input("Enter New PIN: "))

            confirm_pin = int(input("Confirm New PIN: "))

            if new_pin == confirm_pin:

                correct_pin = new_pin

                print("PIN Changed Successfully")

            else:

                print("PIN Does Not Match")

        else:

            print("Incorrect Old PIN")

    # ========================================================
    # INVALID MENU OPTION
    # ========================================================

    else:

        print("Invalid ATM Option")

# ============================================================
# WRONG PIN
# ============================================================

else:

    print("Incorrect PIN")

    print("Transaction Cancelled")

print("\n=========== THANK YOU FOR USING ATM ===========")