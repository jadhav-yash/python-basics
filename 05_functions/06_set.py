# =========================================================
# PYTHON SET METHODS 
# =========================================================

students = {"Rahul", "Amit", "Sneha"}

print("\nORIGINAL SET:")
print(students)


# =========================================================
# 1. add()
# Adds ONE item into set
# =========================================================

print("\n1. add()")

students.add("Priya")

print("After add():", students)


# =========================================================
# 2. update()
# Adds MULTIPLE items into set
# =========================================================

print("\n2. update()")

students.update(["Karan", "Neha"])

print("After update():", students)


# =========================================================
# 3. remove()
# Removes item from set
# If item not found -> Error
# =========================================================

print("\n3. remove()")

students.remove("Amit")

print("After remove():", students)


# =========================================================
# 4. discard()
# Removes item safely
# If item not found -> NO Error
# =========================================================

print("\n4. discard()")

students.discard("Unknown Student")

print("After discard():", students)


# =========================================================
# 5. pop()
# Removes RANDOM item from set
# Because set is unordered
# =========================================================

print("\n5. pop()")

removed_item = students.pop()

print("Removed Item:", removed_item)
print("After pop():", students)


# =========================================================
# 6. clear()
# Removes ALL items from set
# =========================================================

print("\n6. clear()")

temp_set = {1, 2, 3}

print("Before clear():", temp_set)

temp_set.clear()

print("After clear():", temp_set)


# =========================================================
# 7. union()
# Combines two sets
# Duplicate values removed automatically
# =========================================================

print("\n7. union()")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print("Union Result:", result)


# =========================================================
# 8. intersection()
# Finds COMMON values between sets
# =========================================================

print("\n8. intersection()")

common = set1.intersection(set2)

print("Common Values:", common)


# =========================================================
# 9. difference()
# Finds values present in first set but not second
# =========================================================

print("\n9. difference()")

difference_result = set1.difference(set2)

print("Difference Result:", difference_result)


# =========================================================
# 10. issubset()
# Checks whether one set is inside another set
# Returns True or False
# =========================================================

print("\n10. issubset()")

small_set = {1, 2}

print("Is subset?:", small_set.issubset(set1))


# =========================================================
# 11. issuperset()
# Checks whether set contains another complete set
# =========================================================

print("\n11. issuperset()")

print("Is superset?:", set1.issuperset(small_set))


# =========================================================
# DUPLICATE REMOVAL EXAMPLE
# =========================================================

print("\n========== DUPLICATE REMOVAL ==========")

numbers = [10, 20, 10, 30, 20, 40]

print("Original List:", numbers)

unique_numbers = set(numbers)

print("After Removing Duplicates:", unique_numbers)