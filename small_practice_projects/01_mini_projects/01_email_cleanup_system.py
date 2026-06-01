print("============================================")
print("            EMAIL CLEANUP SYSTEM            ")
print("============================================")

email = input("Enter your email for cleaning: ")

new_email = email.lower().strip().replace(" ","")
final_email = new_email.endswith("@gmail.com")

print("Original email:", email)
print()

if final_email == True :
    print("Cleaned email:", new_email)
else :
    print("Email should end with '@gmail.com' !!!")