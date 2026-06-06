# ==========================================
# POLYMORPHISM
# ==========================================

print("===== Example 1 =====")

class Cat:

    def sound(self):
        print("Cat Says Meow")


class Dog:

    def sound(self):
        print("Dog Says Bark")


# Same method name
# Different behavior

c = Cat()
d = Dog()

c.sound()
d.sound()

class Rectangle:
    def area(self, length, width):
        return length * width
    


print("\n===== Example 2 =====")

class Circle:
    def area(self, radius):
        return 3.14 * radius * radius


class Triangle:
    def area(self, base, height):
        return 0.5 * base * height


r = Rectangle()
c = Circle()
t = Triangle()

print("Rectangle Area:", r.area(10, 5))
print("Circle Area:", c.area(7))
print("Triangle Area:", t.area(6, 4))