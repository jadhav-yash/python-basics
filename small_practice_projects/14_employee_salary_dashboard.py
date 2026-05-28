print("============================================")
print("          EMPLOYEE SALARY DASHBOARD         ")
print("============================================")

employee = {
    "Salary" : 50000,
    "Bonus" : 5000,
    "Tax" : 3000,
    "Deduction" : 1000
}

for key,value in employee.items() :
    print(key,":",value)

total_bonus = employee["Bonus"]
total_deduction = employee["Tax"] + employee["Deduction"]
final_salary = employee["Salary"] + total_bonus - total_deduction
print("Final Salary :", final_salary)
print()