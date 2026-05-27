# =========================================================
# PYTHON STRING METHODS
# =========================================================

text = "   python programming language   "

print("\nORIGINAL STRING:")
print(text)


# =========================================================
# 1. upper()
# Converts all letters into CAPITAL letters
# =========================================================

print("\n1. upper()")

upper_text = text.upper()

print("After upper():", upper_text)


# =========================================================
# 2. lower()
# Converts all letters into small letters
# =========================================================

print("\n2. lower()")

lower_text = upper_text.lower()

print("After lower():", lower_text)


# =========================================================
# 3. strip()
# Removes extra spaces from left and right side
# Very useful in forms, login systems, user input cleaning
# =========================================================

print("\n3. strip()")

clean_text = text.strip()

print("Before strip():", text)
print("After strip():", clean_text)


# =========================================================
# 4. replace()
# Replaces old word with new word
# =========================================================

print("\n4. replace()")

new_text = clean_text.replace("python", "java")

print("After replace():", new_text)


# =========================================================
# 5. find()
# Finds position/index of a word or character
# If not found -> returns -1
# =========================================================

print("\n5. find()")

position = clean_text.find("programming")

print("Position of 'programming':", position)


# =========================================================
# 6. split()
# Converts string into list using separator
# By default separator is space
# =========================================================

print("\n6. split()")

words = clean_text.split()

print("After split():", words)
print("Datatype:", type(words))


# =========================================================
# 7. join()
# Combines list items into one string
# =========================================================

print("\n7. join()")

joined_text = "-".join(words)

print("After join():", joined_text)


# =========================================================
# 8. startswith()
# Checks whether string starts with specific word
# Returns True or False
# =========================================================

print("\n8. startswith()")

result = clean_text.startswith("python")

print("Does string start with 'python'? :", result)


# =========================================================
# 9. endswith()
# Checks whether string ends with specific word
# Returns True or False
# =========================================================

print("\n9. endswith()")

result = clean_text.endswith("language")

print("Does string end with 'language'? :", result)