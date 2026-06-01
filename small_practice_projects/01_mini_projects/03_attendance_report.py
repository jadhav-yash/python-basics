print("============================================")
print("              ATTENDANCE REPORT             ")
print("============================================")

attendance = ["P","A","P","P","L","P","A","P","P","L"]
print("Attendance Data :", attendance)
print()

present_days = attendance.count("P")
absent_days = attendance.count("A")
leave_days = attendance.count("L")
working_records = present_days + absent_days + leave_days

print("Total Present Days: ", present_days)
print("Total Absent Days: ", absent_days)
print("Total Leave Days: ", leave_days)
print("Total Working Records: ", working_records)