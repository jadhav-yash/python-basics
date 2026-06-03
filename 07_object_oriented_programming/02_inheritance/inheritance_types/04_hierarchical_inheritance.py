# Multiple Child classes inherit from One Parent class.

# ==========================================
# HIERARCHICAL INHERITANCE
# ==========================================

class Vehicle:

    def start(self):

        print("Vehicle Starts")


class Car(Vehicle):

    def car_feature(self):

        print("Car has AC")


class Bike(Vehicle):

    def bike_feature(self):

        print("Bike gives mileage")


c = Car()

b = Bike()

c.start()

c.car_feature()

b.start()

b.bike_feature()