# =========================================================
# Arithmetic operators
# =========================================================
print("\nARITHMETIC Operators:")
a = 3
b = 2
print("a :", a)
print("b :", b)
print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division(Removes decimal) :", a // b)
print("Modulus(Remainder) :", a % b)
print("Power :", a ** b)

# =========================================================
# Assignment operators
# =========================================================
print("\nASSIGNMENT Operators:")
x = 10
print("x :", x)
# Add and assign
x += 5
print("After x += 5 :", x)
# Subtract and assign
x -= 3
print("After x -= 3 :", x)
# Multiply and assign
x *= 2
print("After x *= 2 :", x)
# Divide and assign
x /= 4
print("After x /= 4 :", x)
# Floor divide and assign
x //= 2
print("After x //= 2 :", x)
# Modulus and assign
x %= 3
print("After x %= 3 :", x)
# Power and assign  
x **= 2
print("After x **= 2 :", x)

# =========================================================
# Comparison operators
# =========================================================
print("\nCOMPARISON Operators:")
num1 = 10
num2 = 20
print("num1 :", num1)
print("num2 :", num2)
# Equal to
print("num1 == num2 :", num1 == num2)
# Not equal to
print("num1 != num2 :", num1 != num2)
# Greater than
print("num1 > num2 :", num1 > num2)
# Less than
print("num1 < num2 :", num1 < num2)
# Greater than or equal to
print("num1 >= num2 :", num1 >= num2)
# Less than or equal to
print("num1 <= num2 :", num1 <= num2)

# =========================================================
# Logical operators
# =========================================================
print("\nLOGICAL Operators:")
is_raining = True
is_weekend = False
print("Is Raining :", is_raining)
print("Is Weekend :", is_weekend)
# AND
print("Is it Raining AND Weekend ?", is_raining and is_weekend)
# OR
print("Is it Raining OR Weekend ?", is_raining or is_weekend)
# NOT
print("Is it NOT Raining ?", not is_raining)

# =========================================================
# Membership operators
# =========================================================
print("\nMEMBERSHIP Operators:")
fruits = ["apple", "banana", "cherry"]
print("Fruits :", fruits)
# in
print("Is 'apple' in fruits ?", "apple" in fruits)
# not in
print("Is 'mango' not in fruits ?", "mango" not in fruits)

# =========================================================
# Identity operators
# =========================================================
print("\nIDENTITY Operators:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("List1 :", list1)
print("List2 :", list2)
# is
print("Does list1 is list2 ?", list1 is list2)
# is not
print("Does list1 is not list2 ?", list1 is not list2)

# =========================================================
# Bitwise operators
# =========================================================
print("\nBITWISE Operators:")
n1 = 5  # In binary: 0101
n2 = 3  # In binary: 0011
print("n1 :", n1)
print("n2 :", n2)
# AND
print("n1 & n2 :", n1 & n2)
# OR
print("n1 | n2 :", n1 | n2)
# XOR
print("n1 ^ n2 :", n1 ^ n2)
# NOT
print("~n1 :", ~n1)
# Left Shift
print("n1 << 1 :", n1 << 1)
# Right Shift
print("n1 >> 1 :", n1 >> 1)
