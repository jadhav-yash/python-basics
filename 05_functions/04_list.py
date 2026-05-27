# =========================================================
# PYTHON LIST METHODS
# =========================================================

students = ["Rahul", "Amit", "Sneha"]

print("\nORIGINAL LIST:")
print(students)


# =========================================================
# 1. append()
# Adds ONE item at the END of list
# =========================================================

print("\n1. append()")

students.append("Priya")

print("After append():", students)


# =========================================================
# 2. extend()
# Adds MULTIPLE items into list
# =========================================================

print("\n2. extend()")

students.extend(["Karan", "Neha"])

print("After extend():", students)


# =========================================================
# 3. insert()
# Adds item at specific position/index
# Syntax:
# list.insert(index, value)
# =========================================================

print("\n3. insert()")

students.insert(1, "Vikas")

print("After insert():", students)


# =========================================================
# 4. remove()
# Removes item using VALUE
# If value not found -> Error
# =========================================================

print("\n4. remove()")

students.remove("Amit")

print("After remove():", students)


# =========================================================
# 5. pop()
# Removes item using INDEX
# If no index given -> removes LAST item
# =========================================================

print("\n5. pop()")

removed_student = students.pop()

print("Removed Student:", removed_student)
print("After pop():", students)


# =========================================================
# 6. clear()
# Removes ALL items from list
# =========================================================

print("\n6. clear()")

temp_list = [1, 2, 3]

print("Before clear():", temp_list)

temp_list.clear()

print("After clear():", temp_list)


# =========================================================
# 7. sort()
# Sorts list in ascending order
# =========================================================

print("\n7. sort()")

numbers = [50, 10, 40, 20, 30]

print("Before sort():", numbers)

numbers.sort()

print("After sort():", numbers)


# =========================================================
# 8. reverse()
# Reverses list order
# =========================================================

print("\n8. reverse()")

numbers.reverse()

print("After reverse():", numbers)


# =========================================================
# 9. copy()
# Creates duplicate copy of list
# =========================================================

print("\n9. copy()")

new_numbers = numbers.copy()

print("Original List:", numbers)
print("Copied List:", new_numbers)


# =========================================================
# 10. count()
# Counts how many times value exists
# =========================================================

print("\n10. count()")

marks = [90, 80, 90, 70, 90]

count_90 = marks.count(90)

print("90 appears", count_90, "times")


# =========================================================
# 11. index()
# Finds position/index of value
# =========================================================

print("\n11. index()")

position = students.index("Sneha")

print("Position of Sneha:", position)