# ==============================================================
# 30 Scenario-Based Questions on Operators
# ==============================================================

# 1. School Fee Calculator
monthly_fee = 1500    
months = 3
total_fee = monthly_fee * months
print("1. Total fee:", total_fee)

# 2. Chocolate Sharing
chocolates = 40
students = 8
chocolates_per_student = chocolates // students
print("2. Chocolates per student:", chocolates_per_student)

# 3. Remaining Chocolates
chocolates = 43
students = 8
remaining_chocolates = chocolates % students
print("3. Remaining chocolates:", remaining_chocolates)

# 4. Student Pass Check
marks = 37 
passing_marks = 35
print("4. Is student passed?", marks >= passing_marks)

# 5. Age Eligibility
age = int(input("5. Enter student's age: "))
print("5. Is student eligible for joining coding workshop?", age >= 12)
    
# 6. Shopping Total
bag = 700
shoes = 1200
total_bill = bag + shoes
print("6. Total bill:", total_bill)

# 7. Discount Calculation
product_price = 2000
discount = 300
final_price = product_price - discount
print("7. Final price after discount:", final_price)

# 8. Pocket Money Update
student_money = 500
parents_money = 200
student_money += parents_money
print("8. Total pocket money:", student_money)

# 9. Pen Distribution
pens = 60
pen_per_student = 5
students = pens // pen_per_student
print("9. Number of students that can receive pens:", students)

# 10. Even or Odd Roll Number
roll_number = 24
print("10. Is roll number even?", roll_number % 2 == 0)
print("10. Is roll number odd?", roll_number % 2 != 0)

# 11. Exam Result Message
marks = 35
passing_marks = 35
print("11. Are you passed?", marks >= passing_marks)

# 12. Mobile Battery 
phone_battery = 80
after_gaming = 25
phone_battery -= after_gaming
print("12. Phone battery percentage after gaming:", phone_battery)

# 13. Game Score
score = 100
bonus = 50
score += bonus
print("13. Total score after bonus:", score)

# 14. Password Match
correct_password = "python123"
user_input = input("14. Enter your password: ")
print("14. Password are same?", correct_password == user_input)

# 15. Wrong Password Check
correct_password = "admin123"
user_input = "admin"
print("15. Password is not correct?", correct_password != user_input)

# 16. Movie Ticket Cost
ticket_cost = 180
friends = 4
total_ticket_cost = ticket_cost * friends
print("16. Total cost for movie tickets:", total_ticket_cost)

# 17. Fuel Cost
bike_petrol = 2
petrol_price = 105
total_petrol_cost = bike_petrol * petrol_price
print("17. Total fuel cost:", total_petrol_cost)

# 18. Temperature Check
classroom_temperature = 38
print("18. Is the classroom temperature high?", classroom_temperature > 35)

# 19. Height Comparison
studentA_height = 150
studentB_height = 145
print("19. Is student A taller than student B?", studentA_height > studentB_height)

# 20. Same Marks Check
studentA_marks = 88
studentB_marks = 88
print("20. Do both students have the same marks?", studentA_marks == studentB_marks)

# 21. Attendance Eligibility
student = 74
print("21. Is student eligible for exam?", student >= 75)

# 22. Book Price After Offer
book_cost = 500
offer_price = 50
new_book_price = book_cost - offer_price
print("22. New book price after offer:", new_book_price)

# 23. Monthly Savings
student_savings = 100
weeks = 4
total_savings = student_savings * weeks
print("23. Total savings:", total_savings)

# 24. Water Bottles
bottles = 25
each_table = 4
tables = bottles // each_table
print("24. Number of tables that can be filled:", tables)
print("24. Leftover bottles:", bottles % each_table)

# 25. Classroom Chairs 
students = 36
chairs = 30
print("25. Are there enough chairs for all students?", chairs >= students)

# 26. Simple Salary Update
salary = 15000
increment = 2000
salary += increment
print("26. Updated salary after increment:", salary)

# 27. Online Cart Quantity
cart_notebooks = 2
added_notebooks = 3
quantity = cart_notebooks + added_notebooks
print("27. Total notebooks in cart:", quantity)

# 28. Comparing Product Prices
pen_price = 10
pencil_price = 5
print("28. Is pen costlier?", pen_price > pencil_price)

# 29. Marks Percentage
marks_obtained = 420
total_marks = 500
percentage = (marks_obtained / total_marks) * 100
print("29. Marks percentage:", percentage)

# 30. Final Bill With GST
product_cost = 1000
gst = 18
gst_amount = (product_cost * gst) / 100
print("30. GST amount:", gst_amount)
final_bill = product_cost + gst_amount
print("30. Final bill:", final_bill)

# ==============================================================
# Advanced Scenario-Based Questions on Operators
# ==============================================================

# 1.
order_amount = int(input("1. Enter order amount: "))
membership = input("1. Do you have a premium membership? (yes/no): ")
if order_amount > 499 and membership == "yes":
    print("1. You are eligible for free delivery.")
else:
    print("1. You are not eligible for free delivery.")

# 2.
account_balance = int(input("2. Enter your account balance: "))
withdrawal_amount = int(input("2. Enter withdrawal amount: "))
if account_balance > withdrawal_amount:
    print("2. Withdrawal successful.")
else:
    print("2. Insufficient balance.")

# 3.
marks = int(input("3. Enter your marks: "))
competition = input("3. Did you won a national competition? (yes/no): ")
if marks > 85 or competition == "yes":
    print("3. You are eligible for a scholarship.")
else:
    print("3. You are not eligible for a scholarship.")

# 4.
movie_ticket_price = 200
weekends = input("4. Is it a weekend? (yes/no): ")
if weekends == "yes":
    movie_ticket_price *= 2
    print("4. Movie ticket price:", movie_ticket_price)
else:
    print("4. Movie ticket price:", movie_ticket_price)

# 5.
username = "admin"
password = "admin123"
input_username = input("5. Enter username: ")
input_password = input("5. Enter password: ")
if input_username == username and input_password == password:
    print("5. Exam portal login successful.")
else:
    print("5. Exam portal login failed.")

# 6.
product_price = 5000
discount = 100
after_discount = product_price - discount
gst = 18
final_price = after_discount + (after_discount * gst / 100)
print("6. Final price after discount and GST:", final_price)

# 7.
player_health = 200
attack_damage = 20
player_health -= attack_damage
print("7. Player health after attack:", player_health)

# 8.
age = int(input("8. Enter your age: "))
if age < 10 or age > 60:
    print("8. You are eligible for emergency treatment.")
else:
    print("8. You are not eligible for emergency treatment.")

# 9.
slots_available = 5
if slots_available > 0:
    print("9. Parking slots available.")
else:
    print("9. No parking slots available.")

# 10.
attendance = int(input("10. Enter your attendance percentage: "))
if attendance >= 75:
    print("10. You can participate in the sports.")
else:
    print("10. You cannot participate in the sports.")

# 11.
purchase_amount = int(input("11. Enter purchase amount: "))
if purchase_amount > 10000:
    print("11. You are eligible for extra cashback.")
else:
    print("11. You are not eligible for extra cashback.")

# 12.
seats_available = 3
if seats_available > 0:
    print("12. Seats are available for booking the ticket.")
else:
    print("12. No seats available for booking the ticket.")

# 13.
restaurant_bill = 4137 
friends = 5
bill_per_person = restaurant_bill // friends
print("13. Bill per person:", bill_per_person)
remaining_amount = restaurant_bill % friends
print("13. Remaining amount after splitting the bill:", remaining_amount)

# 14.
face_recognition = input("14. Is face recognition successful? (yes/no): ")
fingerprint_verification = input("14. Is fingerprint verification successful? (yes/no): ")
if face_recognition == "yes" and fingerprint_verification == "yes":
    print("14. Smart door unlocked.")
else:
    print("14. Smart door locked.")

# 15.
subscriber_count = int(input("15. Enter your YouTube channel subscriber count: "))
if subscriber_count >= 100000:
    print("15. You earned a bonus income.")
else:
    print("15. You did not earn a bonus income.")

# 16.
units = int(input("16. Enter electricity units consumed: "))
extra_units = units - 100
if extra_units > 0:
    extra_charge = extra_units * 8
    print("16. Extra charge for electricity:", extra_charge)
else:
    print("16. No extra charge for electricity.")

# 17.
runs = int(input("17. Enter the runs scored by the player: "))
fitness_score = int(input("17. Enter the fitness score of the player: "))
if runs > 500 and fitness_score > 80:
    print("17. Player is selected for the team.")
else:
    print("17. Player is not selected for the team.")

# 18.
salary = int(input("18. Enter your salary: "))
credit_score = int(input("18. Enter your credit score: "))
if salary > 30000 and credit_score > 700:
    print("18. You are approved for a loan.")
else:
    print("18. You are not approved for a loan.")

# 19.
roll_number = int(input("19. Enter your roll number: "))
if roll_number % 2 == 0:
    print("19. Your roll number belongs to even bench.") 
else:
    print("19. Your roll number belongs to odd bench.")

# 20.
system_otp = "123456"
user_otp = input("20. Enter the OTP sent to your mobile: ")
if user_otp == system_otp:
    print("20. OTP verification successful! You can reset your password.")
else:
    print("20. OTP verification failed! Please try again.")

# 21.
age = int(input("21. Enter your age: "))
if age < 25 or age > 55:
    print("21. You are eligible for a premium membership discounts.")
else:
    print("21. You are not eligible for a premium membership discounts.")

# 22.
total_amount = int(input("22. Enter total amount of your shopping: "))
item_amount = int(input("22. Enter the amount of the item you want to add: "))
total_amount += item_amount
print("22. Updated total amount after adding the item:", total_amount)

# 23.
petrol_cost_per_liter = 105
liters = int(input("23. Enter the number of liters you want to buy: "))
total_cost = petrol_cost_per_liter * liters
print("23. Total cost of petrol:", total_cost)

# 24.
laptop_battery = int(input("24. Enter your laptop battery percentage: "))
if laptop_battery < 15:
    print("24. Your laptop battery is low. Please turn on power saving mode.")
else:
    print("24. Your laptop battery is sufficient for use.")

# 25.
monthly_salary = int(input("25. Enter your monthly salary: "))
multiplier = 4
bonus = monthly_salary * multiplier
print("25. Your bonus amount is:", bonus)