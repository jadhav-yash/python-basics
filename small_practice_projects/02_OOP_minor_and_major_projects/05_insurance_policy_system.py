# =============================================
# INSURANCE POLICY SYSTEM
# =============================================

class Insurance:

    def __init__(self, policy_number, customer_name, premium_amount):
        self.policy_number = policy_number
        self.customer_name = customer_name
        self.premium_amount = premium_amount

    def display_policy_details(self):
        print("\n=============== INSURANCE POLICY DETAILS ===============")
        print("Policy Number:", self.policy_number)
        print("Customer Name:", self.customer_name)
        print("Premium Amount:", self.premium_amount)

class HealthInsurance(Insurance):

    def __init__(self, policy_number, customer_name, premium_amount, coverage_hospital_bills):
        super().__init__(policy_number, customer_name, premium_amount)
        self.coverage_hospital_bills = coverage_hospital_bills

    def display_health_insurance_details(self):
        self.display_policy_details()
        print("Coverage Amount:", self.coverage_hospital_bills)

class VehicleInsurance(Insurance):

    def __init__(self, policy_number, customer_name, premium_amount, coverage_accident_damage):
        super().__init__(policy_number, customer_name, premium_amount)
        self.coverage_accident_damage = coverage_accident_damage

    def display_vehicle_insurance_details(self):
        self.display_policy_details()
        print("Coverage Amount:", self.coverage_accident_damage)

class LifeInsurance(Insurance):

    def __init__(self, policy_number, customer_name, premium_amount, maturity_amount):
        super().__init__(policy_number, customer_name, premium_amount)
        self.maturity_amount = maturity_amount

    def display_life_insurance_details(self):
        self.display_policy_details()
        print("Maturity Amount:", self.maturity_amount)

health = HealthInsurance("H123", "Yash", 5000, 100000)
health.display_health_insurance_details()

vehicle = VehicleInsurance("V456", "Utsav", 3000, 50000)
vehicle.display_vehicle_insurance_details()

life = LifeInsurance("L789", "Vishesh", 2000, 150000)
life.display_life_insurance_details()