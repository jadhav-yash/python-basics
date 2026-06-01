# =========================================================
# OBJECT ORIENTED PROGRAMMING IN PYTHON
# =========================================================

# ---------------------------------------------------------
# CLASS
# ---------------------------------------------------------
# Class is a blueprint / design.
# It defines what data and behavior an object will have.

class Student:

    # -----------------------------------------------------
    # CONSTRUCTOR
    # -----------------------------------------------------
    # __init__ method is called automatically
    # when we create an object.
    #
    # self means current object.
    # self.name means this object's name.
    # self.age means this object's age.

    def __init__(self, name, age, course):
        self.name = name        # instance variable
        self.age = age          # instance variable
        self.course = course    # instance variable

    # -----------------------------------------------------
    # METHOD
    # -----------------------------------------------------
    # Method is a function inside a class.
    # It represents the behavior of object.

    def show_details(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Student Course:", self.course)

    def study(self):
        print(self.name, "is studying", self.course)


# ---------------------------------------------------------
# OBJECT CREATION
# ---------------------------------------------------------
# Object means real value created from class.

student1 = Student("Rahul", 20, "Python")
student2 = Student("Priya", 22, "Java")

# Calling methods using object

student1.show_details()
student1.study()

print("==============================")

student2.show_details()
student2.study()




# =========================================================
# MOBILE SHOP MANAGEMENT SYSTEM
# =========================================================


# =========================================================
# CLASS
# =========================================================
# Class is a blueprint/design.
# Here Mobile is a class.
# =========================================================

class Mobile:

    # =====================================================
    # CONSTRUCTOR
    # =====================================================
    # __init__() is automatically called
    # when object is created.
    #
    # self = current object
    # =====================================================

    def __init__(self, brand, model, price):

        # Storing values into object variables

        self.brand = brand
        self.model = model
        self.price = price


    # =====================================================
    # METHOD
    # =====================================================
    # Method is a function inside class.
    # This method displays mobile details.
    # =====================================================

    def show_mobile_details(self):

        print("\n======== MOBILE DETAILS ========")

        print("Mobile Brand :", self.brand)

        print("Mobile Model :", self.model)

        print("Mobile Price : ₹", self.price)


    # =====================================================
    # ANOTHER METHOD
    # =====================================================
    # Simulating calling feature
    # =====================================================

    def make_call(self):

        print(self.brand, self.model, "is calling...")


    # =====================================================
    # ANOTHER METHOD
    # =====================================================
    # Simulating camera feature
    # =====================================================

    def open_camera(self):

        print(self.brand, self.model, "camera opened")


# =========================================================
# OBJECT CREATION
# =========================================================
# Creating real mobile objects from class
# =========================================================

mobile1 = Mobile(
    "Samsung",
    "Galaxy S24",
    80000
)

mobile2 = Mobile(
    "Apple",
    "iPhone 15",
    120000
)


# =========================================================
# CALLING METHODS USING OBJECT
# =========================================================

mobile1.show_mobile_details()

mobile1.make_call()

mobile1.open_camera()


# =========================================================
# SECOND OBJECT
# =========================================================

mobile2.show_mobile_details()

mobile2.make_call()

mobile2.open_camera()