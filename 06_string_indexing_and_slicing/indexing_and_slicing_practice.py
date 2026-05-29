# =========================================================
#         PYTHON STRING INDEXING AND SLICING
# =========================================================

# String:
# Collection of characters

# Example:
name = "PYTHON"

print("\nString =", name)

# =========================================================
# INDEXING
# =========================================================

# Indexing means:
# Accessing one character from string

# Python gives position number to every character

# =========================================================
# POSITIVE INDEXING
# =========================================================

#   P   Y   T   H   O   N
#   0   1   2   3   4   5

print("\n========== POSITIVE INDEXING ==========")

print(name[0])   # P
print(name[1])   # Y
print(name[2])   # T
print(name[3])   # H
print(name[4])   # O
print(name[5])   # N

# =========================================================
# NEGATIVE INDEXING
# =========================================================

#   P   Y   T   H   O   N
#  -6  -5  -4  -3  -2  -1

print("\n========== NEGATIVE INDEXING ==========")

print(name[-1])   # N
print(name[-2])   # O
print(name[-3])   # H
print(name[-4])   # T
print(name[-5])   # Y
print(name[-6])   # P

# =========================================================
# SLICING
# =========================================================

# Slicing means:
# Taking multiple characters from string

# Syntax:
# string[start : stop]

# IMPORTANT:
# stop index is NOT included

# =========================================================
# BASIC SLICING
# =========================================================

city = "MUMBAI"

print("\n========== BASIC SLICING ==========")

#  M  U  M  B  A  I
#  0  1  2  3  4  5

print(city[0:3])   # MUM
print(city[0:4])   # MUMB
print(city[1:5])   # UMBA
print(city[2:6])   # MBAI

# =========================================================
# SLICING WITHOUT START
# =========================================================

print("\n========== SLICING WITHOUT START ==========")

print(city[:3])    # MUM

# Python starts from beginning automatically

# =========================================================
# SLICING WITHOUT STOP
# =========================================================

print("\n========== SLICING WITHOUT STOP ==========")

print(city[2:])    # MBAI

# Python goes till end automatically

# =========================================================
# FULL STRING
# =========================================================

print("\n========== FULL STRING ==========")

print(city[:])     # MUMBAI

# =========================================================
# STEP SLICING
# =========================================================

# Syntax:
# string[start : stop : step]

print("\n========== STEP SLICING ==========")

language = "PYTHON"

print(language[0:6:1])   # PYTHON
print(language[0:6:2])   # PTO
print(language[0:6:3])   # PH

# =========================================================
# REVERSE STRING
# =========================================================

print("\n========== REVERSE STRING ==========")

print(language[::-1])    # NOHTYP

# =========================================================
# REAL LIFE EXAMPLE 1
# MOBILE NUMBER MASKING
# =========================================================

print("\n========== MOBILE NUMBER MASKING ==========")

mobile = "9876543210"

# First 2 digits
print(mobile[0:2])

# Last 4 digits
print(mobile[-4:])

# Middle digits
print(mobile[2:6])

# =========================================================
# REAL LIFE EXAMPLE 2
# EMAIL DOMAIN EXTRACTION
# =========================================================

print("\n========== EMAIL DOMAIN EXTRACTION ==========")

email = "student@gmail.com"

print(email[8:17])    # gmail.com

# =========================================================
# REAL LIFE EXAMPLE 3
# WEBSITE NAME EXTRACTION
# =========================================================

print("\n========== WEBSITE NAME EXTRACTION ==========")

website = "www.google.com"

print(website[4:10])   # google

# =========================================================
# REAL LIFE EXAMPLE 4
# ATM CARD LAST 4 DIGITS
# =========================================================

print("\n========== ATM CARD LAST 4 DIGITS ==========")

card = "1234567890123456"

print(card[-4:])   # 3456

# =========================================================
# REAL LIFE EXAMPLE 5
# YOUTUBE VIDEO ID
# =========================================================

print("\n========== YOUTUBE VIDEO ID ==========")

video_id = "YT987654321"

print(video_id[2:])   # 987654321