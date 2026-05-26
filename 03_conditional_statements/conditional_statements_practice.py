# =========================================================
# IF STATEMENT
# =========================================================

print("1) SIMPLE IF STATEMENT")

age = 20

if age >= 18:
    print("You are eligible for voting")

print("----------------------------------")

# =========================================================
# 2) IF-ELSE STATEMENT
# =========================================================

print("2) IF ELSE STATEMENT")

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("----------------------------------")

# =========================================================
# 3) IF-ELIF-ELSE
# =========================================================

print("3) IF ELIF ELSE")

marks = 1

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

print("----------------------------------")

# =========================================================
# 4) NESTED IF
# =========================================================

print("4) NESTED IF")

age = 22
percentage = 85

if age >= 18:

    if percentage >= 80:
        print("Admission Approved")

    else:
        print("Marks too low")

else:
    print("Age not eligible")

print("----------------------------------")

# =========================================================
# 5) COMPARISON OPERATORS
# =========================================================

print("5) COMPARISON OPERATORS")

a = 10
b = 20

if b > a:
    print("b is greater than a")

if a != b:
    print("a and b are not equal")

print("----------------------------------")

# =========================================================
# 6) LOGICAL OPERATORS
# =========================================================

print("6) LOGICAL OPERATORS")

username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login Successful")

else:
    print("Invalid Username or Password")

print()


day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("Weekend")

else:
    print("Working Day")

print()


is_logged_in = False

if not is_logged_in:
    print("Please Login")

print("----------------------------------")

# =========================================================
# 7) SHORT HAND IF
# =========================================================

print("7) SHORT HAND IF")

salary = 50000

if salary > 30000: print("Good Salary")

print("----------------------------------")

# =========================================================
# 8) TERNARY OPERATOR
# =========================================================

print("8) TERNARY OPERATOR")

age = 16

result = "Adult" if age >= 18 else "Minor"

print(result)

print("----------------------------------")