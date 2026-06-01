print("============================================")
print("              EMPLOYEE DETAILS              ")
print("============================================")

employee_details = {
    "Name" : "Alex",
    "Department" : "IT",
    "Salary" : 45000,
    "Experience" : 2,
    "Email" : "alex@gmail.com"
}

for key,value in employee_details.items():
    print(key,":",value)