# =========================================================
# PYTHON DICTIONARY METHODS
# =========================================================

student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python",
    "marks": 85
}

print("\nORIGINAL DICTIONARY:")
print(student)


# =========================================================
# ACCESSING VALUES
# =========================================================

print("\n========== ACCESSING VALUES ==========")

print("Student Name:", student["name"])

print("Student Age:", student["age"])


# =========================================================
# 1. get()
# Safely gets value using key
# If key not found -> returns None
# =========================================================

print("\n1. get()")

print("Course:", student.get("course"))

print("Phone:", student.get("phone"))


# =========================================================
# 2. keys()
# Returns all keys
# =========================================================

print("\n2. keys()")

all_keys = student.keys()

print("Dictionary Keys:", all_keys)


# =========================================================
# 3. values()
# Returns all values
# =========================================================

print("\n3. values()")

all_values = student.values()

print("Dictionary Values:", all_values)


# =========================================================
# 4. items()
# Returns key-value pairs
# =========================================================

print("\n4. items()")

all_items = student.items()

print("Dictionary Items:", all_items)


# =========================================================
# 5. update()
# Updates existing value
# OR adds new key-value pair
# =========================================================

print("\n5. update()")

student.update({"marks": 95})

print("After Updating Marks:", student)

student.update({"city": "Mumbai"})

print("After Adding City:", student)


# =========================================================
# 6. pop()
# Removes item using key
# =========================================================

print("\n6. pop()")

removed_value = student.pop("age")

print("Removed Value:", removed_value)

print("After pop():", student)


# =========================================================
# 7. popitem()
# Removes LAST inserted item
# =========================================================

print("\n7. popitem()")

last_item = student.popitem()

print("Removed Last Item:", last_item)

print("After popitem():", student)


# =========================================================
# 8. copy()
# Creates duplicate copy of dictionary
# =========================================================

print("\n8. copy()")

new_student = student.copy()

print("Original Dictionary:", student)

print("Copied Dictionary:", new_student)


# =========================================================
# 9. clear()
# Removes all items from dictionary
# =========================================================

print("\n9. clear()")

temp_dict = {
    "a": 1,
    "b": 2
}

print("Before clear():", temp_dict)

temp_dict.clear()

print("After clear():", temp_dict)


# =========================================================
# LOOPING THROUGH DICTIONARY
# =========================================================

print("\n========== LOOP THROUGH DICTIONARY ==========")

employee = {
    "id": 101,
    "name": "Amit",
    "salary": 50000
}

for key, value in employee.items():

    print(key, ":", value)


# =========================================================
# CHECK KEY EXISTS
# =========================================================

print("\n========== CHECK KEY ==========")

print("Is 'name' Present?:", "name" in employee)

print("Is 'phone' Present?:", "phone" in employee)


# =========================================================
# NESTED DICTIONARY EXAMPLE
# =========================================================

print("\n========== NESTED DICTIONARY ==========")

college = {
    "student1": {
        "name": "Rahul",
        "marks": 90
    },

    "student2": {
        "name": "Sneha",
        "marks": 95
    }
}

print(college)

print("\nStudent1 Name:", college["student1"]["name"])