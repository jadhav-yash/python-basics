print("============================================")
print("        FOOD DELIVERY BILLING SYSTEM        ")
print("============================================")

food_prices = {
    "Burger" : 150,
    "Pizza" : 300,
    "Cold Drink" : 50
}

for key,value in food_prices.items() :
    print(key,":",value)

total_bill = food_prices["Burger"] + food_prices["Pizza"] + food_prices["Cold Drink"]
print()
print("Total Bill :", total_bill)

tax = 18 / 100
tax_amount = total_bill * tax
print("Tax Amount :", tax_amount)

final_amount = total_bill + tax_amount
print("Final Payable Amount :", final_amount)