# =========================================================
# PYTHON TUPLE METHODS
# =========================================================

students = ("Rahul", "Amit", "Sneha", "Rahul")

print("\nORIGINAL TUPLE:")
print(students)


# =========================================================
# 1. count()
# Counts how many times value exists
# =========================================================

print("\n1. count()")

rahul_count = students.count("Rahul")

print("Rahul appears", rahul_count, "times")


# =========================================================
# 2. index()
# Finds position/index of value
# =========================================================

print("\n2. index()")

position = students.index("Sneha")

print("Position of Sneha:", position)


# =========================================================
# ACCESSING TUPLE VALUES
# =========================================================

print("\n========== ACCESSING VALUES ==========")

print("First Student:", students[0])

print("Second Student:", students[1])

print("Last Student:", students[-1])


# =========================================================
# LOOPING THROUGH TUPLE
# =========================================================

print("\n========== LOOP THROUGH TUPLE ==========")

for student in students:

    print(student)


# =========================================================
# TUPLE LENGTH
# =========================================================

print("\n========== LENGTH OF TUPLE ==========")

print("Total Students:", len(students))


# =========================================================
# CHECK VALUE EXISTS OR NOT
# =========================================================

print("\n========== CHECK VALUE ==========")

print("Is Amit Present?:", "Amit" in students)

print("Is Karan Present?:", "Karan" in students)


# =========================================================
# TUPLE CONCATENATION
# Combining two tuples
# =========================================================

print("\n========== CONCATENATION ==========")

tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Combined Tuple:", result)


# =========================================================
# TUPLE REPEAT
# =========================================================

print("\n========== REPEAT TUPLE ==========")

numbers = (10, 20)

print(numbers * 3)