# Grandparent → Parent → Child

# ==========================================
# MULTILEVEL INHERITANCE
# ==========================================

class Animal:

    def eat(self):

        print("Animal Eats")


class Dog(Animal):

    def bark(self):

        print("Dog Barks")


class Puppy(Dog):

    def weep(self):

        print("Puppy Weeps")


p = Puppy()

p.eat()

p.bark()

p.weep()