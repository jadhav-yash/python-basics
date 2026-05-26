# ===================================================
#           Smart Grocery Billing System 
# ===================================================
print("=========================================")
print("     Welcome to Smart Grocery Store      ")
print("=========================================")
customer_name = input("Enter you name: ")
print("Hello,", customer_name)


total_amount = int(input("\nEnter the total shopping amount: "))

discount = 0
membership_discount = 0
final_amount = total_amount

if total_amount > 5000 :
    discount = total_amount * (20 / 100)
    final_amount = total_amount - discount 
    print("You got 20% discount!")
    print("Total amount after discount: ", final_amount)
elif total_amount > 2000 and total_amount <=5000 :
    discount = total_amount * (10 / 100)
    final_amount = total_amount - discount
    print("You got 10% discount!")
    print("Total amount after discount: ", final_amount)
else :
    print("No discount!")


membership_type = input("\nEnter your membership type (Silver,Gold,None): ")
if membership_type == "gold" or membership_type == "Gold" or membership_type == "GOLD" :
    membership_discount = final_amount * (5 / 100)
    final_amount -= membership_discount
    print("You got extra 5% discount!")
    print("Total amount after membership discount: ", final_amount)
elif membership_type == "silver" or membership_type == "Silver" or membership_type == "SILVER" :
    membership_discount = final_amount * (3 / 100)
    final_amount -= membership_discount
    print("You got extra 3% discount!")
    print("Total amount after membership discount: ", final_amount)
else : 
    print("No discount!")


item_quantity = int(input("\nEnter the number of items you bought: "))
if item_quantity > 10 :
    print("You are eligible for free delivery!")
else :
    print("You are not eligible for free delivery.")


gst = total_amount * (18 / 100)
final_amount += gst
print("\nAfter 18% GST the total amount becomes", final_amount)    


print("\n=========================================")
print("                Final Bill               ")
print("=========================================")
print("Customer name: ", customer_name)
print("Original amount: ", total_amount)
print("Discount amount: ", discount + membership_discount)
print("GST amount: ", gst)
print("Final payable amount: ", final_amount)
print("Delivery status: ", "Free delivery" if item_quantity > 10 else "Standard delivery")
print("=========================================")
print("     Thank you for shopping with us!     ")
print("=========================================")





# ===================================================
#         Hospital Patient Emergency System
# ===================================================
print("\n=========================================")
print("    Welcome to Hospital Patient System   ")
print("=========================================")
patient_name = input("Enter patient name: ")


age = int(input("Enter patient age: "))


temperature = float(input("\nEnter patient temperature: "))
if temperature > 102 :
    print("Patient has high fever!")
else :
    print("Patient temperature is normal.")


oxygen_level = float(input("\nEnter patient oxygen level: "))
if oxygen_level < 90 :
    print("Patient has low oxygen level!")
else :
    print("Patient oxygen level is normal.")


blood_pressure_status = input("\nEnter patient blood pressure status (Normal,High,Low): ")


insurance_status = input("\nDoes the patient have insurance? (Yes/No): ")
if insurance_status == "Yes" or insurance_status == "yes" or insurance_status == "YES" :
    print("You got 15% discount on medical bills!")
else :
    print("No discount on medical bills.")


print("\n=========================================")
print("                Patient Report           ")
print("=========================================")
print("Patient name: ", patient_name)
print("Patient category: ", "High risk" if temperature > 102 or oxygen_level < 90 or blood_pressure_status == "high" or blood_pressure_status == "High" or blood_pressure_status == "HIGH" else "Low risk")
print("Age: ", age)
print("Priority: ", "First priority" if age > 60 else "Second priority")
print("Estimated treatment cost: ", "High" if temperature > 102 or oxygen_level < 90 else "Low")
print("Discount: ", "15% discount" if insurance_status == "Yes" or insurance_status == "yes" or insurance_status == "YES" else "No discount")
print("Final payable amount: ", "High" if temperature > 102 or oxygen_level < 90 else "Low")
print("=========================================")
print("    Thank you for using our services!    ")
print("=========================================")





# ===================================================
#             Online Food Delivery App  
# ===================================================
print("\n=========================================")
print("       Welcome to Food Delivery App      ")
print("=========================================")
restaurant_name = input("Enter restaurant name: ")


food_item = input("Enter food item: ")


quantity = int(input("\nEnter quantity: "))
if quantity > 5 :
    print("Bulk order 5% discount!")
else: 
    print("You quantity is less than 5, No Discount!")


distance_km = float(input("\nEnter delivery distance in km: "))
if distance_km > 5 :
    print("Extra delivery charge applies.")
else:
    print("Free delivery!")


coupon_code = input("\nEnter coupon code (if any): ")
if coupon_code == "FOOD50" :
    print("You got ₹50 off with coupon code!")
else:
    print("Invalid coupon code!")


payment_mode = input("\nEnter payment mode (Card/Cash/UPI): ")
if payment_mode == "upi" or payment_mode == "Upi" or payment_mode == "UPI" :
    print("You got 5% cashback on total bill!")
else:
    print("Not applicable for cashback.")


print("\n=========================================")
print("              Order Summary              ")
print("=========================================")
print("Restaurant name: ", restaurant_name)
print("Food item: ", food_item)
print("Quantity: ", quantity)
print("Total bill: ", "Calculated based on food item and quantity")
print("Delivery charge: ", "Extra delivery charges" if distance_km > 5 else "Free delivery")
print("Discount: ", "5% discount" if quantity > 5 else "No discount" or "₹50 off" if coupon_code == "FOOD50" else "No discount")
print("Cashback: ", "5% cashback" if payment_mode == "upi" or payment_mode == "Upi" or payment_mode == "UPI" else "No Cashback")
print("Final bill: ", "Calculated based on total bill, distance, discounts and cashback")
print("Free item eligibility: ", "If total bill amount will be more than ₹1000 than free desert")
print("=========================================")
print("     Thank you for ordering with us!     ")
print("=========================================")