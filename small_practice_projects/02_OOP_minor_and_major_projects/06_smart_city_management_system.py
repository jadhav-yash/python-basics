class Person:

    def __init__(self, name, age, address, mobile):
        self.name = name
        self.age = age
        self.address = address
        self.mobile = mobile

    def display_info(self):
        print("\n=============== PERSON DETAILS ===============")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Mobile: {self.mobile}")


class Citizen(Person):

    def pay_bill(self, amount):
        print(f"{self.name} paid ₹{amount}")

    def register_complaint(self, complaint):
        print(f"Complaint Registered: {complaint}")

    def track_complaint(self, complaint_status):
        print(f"Tracking Complaint Status: {complaint_status}")


class GovernmentEmployee(Person):

    def __init__(self, name, age, address, mobile,
                 employee_id, department, salary):

        super().__init__(name, age, address, mobile)

        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_info(self):
        super().display_info()

        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: ₹{self.salary}")



class PoliceOfficer(GovernmentEmployee):

    def manage_fir(self):
        print("Managing FIR Records")

    def monitor_cctv(self):
        print("Monitoring CCTV Alerts")

    def control_emergency(self):
        print("Controlling Emergency Response")


class TrafficOfficer(GovernmentEmployee):

    def manage_signals(self):
        print("Managing Traffic Signals")

    def generate_challan(self):
        print("Generating Traffic Challan")

    def monitor_road_cameras(self):
        print("Monitoring Road Cameras")


class ElectricityStaff(GovernmentEmployee):

    def manage_bills(self):
        print("Managing Electricity Bills")

    def monitor_smart_meters(self):
        print("Monitoring Smart Meters")

    def track_power_usage(self):
        print("Tracking Power Usage")


class Admin(GovernmentEmployee):

    def manage_departments(self):
        print("Managing All Departments")

    def generate_reports(self):
        print("Generating Smart City Reports")

    def monitor_city_status(self):
        print("Monitoring Entire City")



class InternetEnabled:

    def connect_internet(self):
        print("Connected to Internet")


class BatteryBackup:

    def battery_status(self):
        print("Battery Backup Available")


class AIMonitoring:

    def analyze_data(self):
        print("AI Monitoring Active")



class SmartDevice:

    def __init__(self, device_name, device_id, location):
        self.device_name = device_name
        self.device_id = device_id
        self.location = location

    def display_status(self):
        print("\n=============== SMART DEVICE STATUS ===============")
        print(f"Device Name: {self.device_name}")
        print(f"Device ID: {self.device_id}")
        print(f"Location: {self.location}")
        print(f"Device {self.device_id} active")


class SmartCamera(
    SmartDevice,
    InternetEnabled,
    BatteryBackup,
    AIMonitoring
):
    pass


class SmartTrafficSignal(
    SmartDevice,
    InternetEnabled,
    BatteryBackup
):
    pass


class SmartMeter(
    SmartDevice,
    InternetEnabled,
    BatteryBackup
):
    pass


class SmartStreetLight(
    SmartDevice,
    InternetEnabled
):
    pass



class Complaint:

    def __init__(self, complaint_id, description):
        self.complaint_id = complaint_id
        self.description = description
        self.status = "Pending"

    def display_complaint(self):
        print("\n=============== COMPLAINT DETAILS ===============")
        print(f"Complaint ID: {self.complaint_id}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")

    def update_status(self, status):
        self.status = status
        print(f"Complaint {self.complaint_id} status updated to: {self.status}")



class DigitalPayment:

    def __init__(self, payment_id, amount):
        self.payment_id = payment_id
        self.amount = amount

    def process_payment(self):
        print("\n=============== PAYMENT DETAILS ===============")
        print(f"Payment ID: {self.payment_id}")
        print(f"Payment of ₹{self.amount} processed")



class EmergencyService:

    def __init__(self, service_name, contact_number):
        self.service_name = service_name
        self.contact_number = contact_number

    def respond(self):
        print("\n=============== EMERGENCY SERVICE ===============")
        print(f"Emergency Service: {self.service_name}")
        print(f"Contact Number: {self.contact_number}")
        print("Emergency Team Dispatched")



class CCTVMonitoring:

    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location

    def generate_alert(self):
        print("\n=============== CCTV ALERT ===============")
        print(f"CCTV Camera ID: {self.camera_id}")
        print(f"Location: {self.location}")
        print("Suspicious Activity Alert")



citizen = Citizen("Yash",21,"Virar","9876543210")

citizen.display_info()
citizen.pay_bill(1500)
citizen.register_complaint("Street light not working")
citizen.track_complaint("In Progress")


police = PoliceOfficer("Rahul",35,"Andheri","8304829409","P101","Police",60000)

police.display_info()
police.manage_fir()
police.monitor_cctv()

admin = Admin("Ajay",40,"Dadar","9123456780","A001","Admin",80000)

admin.display_info()
admin.manage_departments()
admin.monitor_city_status()

camera = SmartCamera("Camera 1","CAM001","Railway Station")

camera.display_status()
camera.connect_internet()
camera.battery_status()
camera.analyze_data()

complaint = Complaint("C001","Garbage not collected")

complaint.display_complaint()
complaint.update_status("Resolved")

payment = DigitalPayment("PAY001", 2500)

payment.process_payment()