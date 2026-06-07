# =============================================
# VEHICLE RENTAL SYSTEM
# =============================================

class Vehicle:

    def __init__(self, vehicle_number, brand, model, rent_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day

    def show_details(self):
        print("\n=============== VEHICLE DETAILS ===============")
        print("Vehicle Number:", self.vehicle_number)
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Rent Per Day:", self.rent_per_day)


class Car(Vehicle):

    def seating_capacity(self):
        print("Seating Capacity: 6 Seater")
    
    def calculate_car_rent(self, days):
        print("Car Rent for", days ,"days:", self.rent_per_day * days)


class Bike(Vehicle):

    def helmet_avail(self):
        print("Helmet Availability: 2 Helmets")

    def calculate_bike_rent(self, days):
        print("Bike Rent for", days ,"days:", self.rent_per_day * days)


class Truck(Vehicle):

    def load_capacity(self):
        print("Load Capacity: 500KG")

    def calculate_truck_rent(self, days):
        print("Truck Rent for", days ,"days:", self.rent_per_day * days)


class Scooter(Vehicle):

    def show_battery_level(self):
        print("Battery Level: 85%")

    def calculate_scooter_rent(self, days):
        print("Scooter Rent for", days ,"days:", self.rent_per_day * days)


car = Car("MH 48 AB 5721", "Toyota", "Corolla", 2200)

car.show_details()
car.seating_capacity()
car.calculate_car_rent(3)

bike = Bike("MH 04 XY 9184", "Honda", "Shine 125", 500)

bike.show_details()
bike.helmet_avail()
bike.calculate_bike_rent(3)

truck = Truck("MH 46 TR 3328", "Tata", "LPT 1613", 5500)

truck.show_details()
truck.load_capacity()
truck.calculate_truck_rent(3)

scooter = Scooter("MH 02 SC 7745", "TVS", "Jupiter", 450)

scooter.show_details()
scooter.show_battery_level()
scooter.calculate_scooter_rent(3)