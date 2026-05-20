print("\n====================================================")
print("      WELCOME TO STUDENT MARKS ANALYSIS SYSTEM      ")
print("====================================================")

# =========================================================
# STUDENT DETAILS
# =========================================================

student_name = input("Enter Student Name : ")
roll_number = int(input("Enter Your Roll Number : "))
class_name = int(input("Enter Your Class : "))
age = int(input("Enter Your Age : "))

print("\nHello", student_name)
print("Roll Number :", roll_number)
print("Class :", class_name)
print("Age :", age)

# =========================================================
# Marks Input
# =========================================================

print("\n========= MARKS INPUT =========")

math = int(input("Enter Math Marks : "))
science = int(input("Enter Science Marks : "))
english = int(input("Enter English Marks : "))
history = int(input("Enter History Marks : "))
computer = int(input("Enter Computer Marks : "))

print("\nMath Marks :", math)
print("Science Marks :", science)
print("English Marks :", english)
print("History Marks :", history)
print("Computer Marks :", computer)

# =========================================================
# ARITHMETIC OPERATORS
# =========================================================

print("\n========= ARITHMETIC OPERATORS =========")

# Addition
total_marks = math + science + english + history + computer
print("Total Marks :", total_marks)

# Subtraction
penalty_marks = 5
final_marks = total_marks - penalty_marks
print("Final Marks After Penalty :", final_marks)

# Division
average_marks = final_marks / 5
print("Average Marks :", average_marks)

# =========================================================
# ASSIGNMENT OPERATORS
# =========================================================

print("\n========= ASSIGNMENT OPERATORS =========")

print("Final Marks :", final_marks)

final_marks -= penalty_marks
print("After Penalty of Attendance :", final_marks)

final_marks += 5
print("Grace Marks :", final_marks)

# =========================================================
# COMPARISON OPERATORS
# =========================================================

print("\n========= COMPARISON OPERATORS =========")

print("Is Final Marks Greater Than 175 ?", final_marks > 175)

print("Is Average Marks Less Than 35 ?", average_marks < 35)

print("Is Final Marks Equal To 300 ?", final_marks == 300)

print("Is Final Marks Not Equal To 300 ?", final_marks != 300)

print("Is student Eligible ?", final_marks >= 150)

print("Is Final Marks Less Than Or Equal To 400 ?", final_marks <= 400)

# =========================================================
# LOGICAL OPERATORS
# =========================================================

print("\n========= LOGICAL OPERATORS =========")

attendance = input("Are You present In all Classes? (yes/no): ")
sports = input("Are You Enrolled In Sports? (yes/no): ")

# AND
if attendance == "yes" and sports == "yes":
    final_marks += 3
    print("Extra Points For Attendance and Sports")

# OR
if attendance == "yes" or sports == "yes":
    final_marks += 3
    print("Extra Points For Either Attendance or Sports")

# NOT
if not(age < 18):
    print("Eligible For Final Year Project")
else:
    print("Not Eligible For Final Year Project")

# =========================================================
# MEMBERSHIP OPERATORS
# =========================================================

print("\n========= MEMBERSHIP OPERATORS =========")

subject_list = ["math", "science", "english", "history", "computer"]

search = input("Search Subject : ")

if search in subject_list:
    print(search, "is Available")
else:
    print(search, "is Not Available")

# not in
if "Biology" not in subject_list:
    print("Biology not in Subject List")

# =========================================================
# IDENTITY OPERATORS
# =========================================================

print("\n========= IDENTITY OPERATORS =========")

student_subjects1 = ["math", "computer"]
student_subjects2 = ["math", "computer"]

student_subjects3 = student_subjects1

# Same memory?
print("student_subjects1 is student_subjects3 :", student_subjects1 is student_subjects3)

# Different memory?
print("student_subjects1 is student_subjects2 :", student_subjects1 is student_subjects2)

# Not same object?
print("student_subjects1 is not student_subjects2 :", student_subjects1 is not student_subjects2)

# =========================================================
# FINAL STUDENTS REPORT
# =========================================================

print("\n========= FINAL REPORT =========")

print("Student Name :", student_name)
print("Roll Number :", roll_number)
print("Class :", class_name)
print("Age :", age)
print("Total Marks :", total_marks)
print("Average Marks :", average_marks)
print("Final Marks :", final_marks)

print("\n==============================================================")
print("      Thank You for Using Student Marks Analysis System!")
print("==============================================================")