# =========================================================
# BASIC BOOLEAN VALUES
# =========================================================

print("\n========== BOOLEAN VALUES ==========")

is_logged_in = True

is_payment_done = False

print("Is Logged In?:", is_logged_in)

print("Is Payment Done?:", is_payment_done)

print("Datatype:", type(is_logged_in))


# =========================================================
# COMPARISON OPERATORS
# Result always True or False
# =========================================================

print("\n========== COMPARISON OPERATORS ==========")

a = 10
b = 20

print("a == b :", a == b)

print("a != b :", a != b)

print("a > b :", a > b)

print("a < b :", a < b)

print("a >= b :", a >= b)

print("a <= b :", a <= b)


# =========================================================
# LOGICAL OPERATORS
# and / or / not
# =========================================================

print("\n========== LOGICAL OPERATORS ==========")

age = 25
has_id_card = True

print("\nAND Operator:")

print(age >= 18 and has_id_card)


print("\nOR Operator:")

print(age >= 18 or has_id_card)


print("\nNOT Operator:")

print(not has_id_card)


# =========================================================
# BOOLEAN IN IF CONDITION
# =========================================================

print("\n========== IF CONDITION ==========")

is_raining = True

if is_raining:

    print("Take Umbrella")

else:

    print("No Need For Umbrella")


# =========================================================
# BOOLEAN USING INPUT
# =========================================================

print("\n========== LOGIN SYSTEM ==========")

username = "admin"
password = "1234"

entered_username = "admin"
entered_password = "1234"

is_valid_login = (
    entered_username == username and
    entered_password == password
)

print("Login Success?:", is_valid_login)


# =========================================================
# BOOLEAN WITH LIST
# =========================================================

print("\n========== BOOLEAN WITH LIST ==========")

cart = ["Pizza", "Burger"]

print("Is Pizza in Cart?:", "Pizza" in cart)

print("Is Ice Cream in Cart?:", "Ice Cream" in cart)


# =========================================================
# BOOLEAN USING EMPTY VALUES
# =========================================================

print("\n========== EMPTY VALUES ==========")

print(bool(""))

print(bool(0))

print(bool([]))    

print(bool(None))      

print(bool("Python"))  

print(bool(100))     


# =========================================================
# BOOLEAN FLAGS
# =========================================================

print("\n========== BOOLEAN FLAGS ==========")

website_running = True

server_connected = False

print("Website Running?:", website_running)

print("Server Connected?:", server_connected)