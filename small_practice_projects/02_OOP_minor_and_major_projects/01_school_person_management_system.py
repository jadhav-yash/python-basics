# =============================================
# SCHOOL PERSON MANAGEMENT SYSTEM
# =============================================

class Person:

    def __init__(self, name, age, mobile_no, address):
        self.name = name
        self.age = age
        self.mobile_no = mobile_no
        self.address = address

    def show_details(self):
        print("\n=============== PERSON DETAILS ===============")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile Number:", self.mobile_no)
        print("Address:", self.address)


class Student(Person):

    def attend_class(self):
        print("Student attends the class.")

    def submit_hw(self):
        print("Student submits the homework.")

    def view_marks(self):
        print("Student views his marks.")


class Teacher(Person):

    def take_lecture(self):
        print("Teacher takes the lecture.")

    def check_hw(self):
        print("Teacher checks the homework.")

    def upload_marks(self):
        print("Teacher uploads the marks.")


class Principal(Person):

    def manage_school(self):
        print("Principal manages the school.")

    def approve_reports(self):
        print("Principal approves the reports.")


class Clerk(Person):

    def manage_doc(self):
        print("Clerk manages the document.")

    def college_fees(self):
        print("Clerk collects the fees.")


student = Student("Yash", 19, 8329027315, "Vasai")

student.show_details()
student.attend_class()
student.submit_hw()
student.view_marks()


teacher = Teacher("Swati", 24, 9234253984, "Dadar")

teacher.show_details()
teacher.take_lecture()
teacher.check_hw()
teacher.upload_marks()


principal = Principal("Lucose", 37, 7203849371, "Andheri")

principal.show_details()
principal.manage_school()
principal.approve_reports()


clerk = Clerk("Ramesh", 29, 3849394830, "Naigaon")

clerk.show_details()
clerk.manage_doc()
clerk.college_fees()