# Combination of two or more inheritance types.

# Multiple inheritance
# Multilevel inheritance

# ==========================================
# HYBRID INHERITANCE
# ==========================================

class A:

    def show_a(self):

        print("Class A")


class B(A):

    def show_b(self):

        print("Class B")


class C:

    def show_c(self):

        print("Class C")


# Hybrid Inheritance
class D(B, C):

    def show_d(self):

        print("Class D")


obj = D()

obj.show_a()

obj.show_b()

obj.show_c()

obj.show_d()