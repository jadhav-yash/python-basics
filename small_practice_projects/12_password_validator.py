print("============================================")
print("             PASSWORD VALIDATOR             ")
print("============================================")

password = input("Enter Password: ")

has_number = False

for ch in password:
    if ch.isdigit():
        has_number = True

if len(password) >= 8 and has_number:
    print("Valid Password")
else:
    print("Invalid Password")