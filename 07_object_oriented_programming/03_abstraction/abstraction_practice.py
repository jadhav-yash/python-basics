from abc import ABC, abstractmethod

# ==========================================
# ABSTRACT CLASS
# ==========================================

class Restaurant(ABC):

    # Abstract Method
    @abstractmethod
    def show_menu(self):
        pass

    @abstractmethod
    def delivery_time(self):
        pass


# ==========================================
# CHILD CLASS 1
# ==========================================

class PizzaShop(Restaurant):

    def show_menu(self):
        print("Pizza, Burger, Garlic Bread")

    def delivery_time(self):
        print("Delivery in 30 Minutes")


# ==========================================
# CHILD CLASS 2
# ==========================================

class SouthIndianRestaurant(Restaurant):

    def show_menu(self):
        print("Dosa, Idli, Vada")

    def delivery_time(self):
        print("Delivery in 20 Minutes")


# ==========================================
# OBJECT CREATION
# ==========================================

pizza = PizzaShop()
pizza.show_menu()
pizza.delivery_time()

print()

south = SouthIndianRestaurant()

south.show_menu()
south.delivery_time()