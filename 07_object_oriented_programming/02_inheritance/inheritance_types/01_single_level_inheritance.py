# ==========================================
# SINGLE INHERITANCE
# ==========================================

# Parent Class
class Animal:

    def sound(self):

        print("Animals make sound")


# Child Class
class Dog(Animal):

    def bark(self):

        print("Dog barks")


# Object of Child Class
d = Dog()

# Access Parent Method
d.sound()

# Access Child Method
d.bark()