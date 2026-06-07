# =============================================
# SMART DEVICE SYSTEM
# =============================================

class SmartDevice:
    def __init__(self, device_id, brand, power_status = False):
        self.device_id = device_id
        self.brand = brand
        self.power_status = power_status

    def turn_on(self):
        self.power_status = True
        print("\n=============== DEVICE DETAILS ===============")
        print(self.brand, "device", self.device_id, "is now ON.")

    def turn_off(self):
        self.power_status = False
        print("\n=============== DEVICE DETAILS ===============")
        print(self.brand, "device", self.device_id, "is now OFF.")

class SmartLight(SmartDevice):
    def __init__(self, device_id, brand, power_status = False, brightness = 0):
        super().__init__(device_id, brand, power_status)
        self.brightness = brightness

    def set_brightness(self, level):
        if 0 <= level <= 100:
            self.brightness = level
            print(self.brand, "light", self.device_id, "brightness set to", self.brightness, "%.")
        else:
            print("Brightness level must be between 0 and 100.")

class SmartFan(SmartDevice):
    def __init__(self, device_id, brand, power_status = False, speed = 0):
        super().__init__(device_id, brand, power_status)
        self.speed = speed

    def set_speed(self, level):
        if 0 <= level <= 3:
            self.speed = level
            print(self.brand, "fan", self.device_id, "speed set to", self.speed)
        else:
            print("Speed level must be between 0 and 3.")

class SmartAC(SmartDevice):
    def __init__(self, device_id, brand, power_status = False, temperature = 24):
        super().__init__(device_id, brand, power_status)
        self.temperature = temperature

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.temperature = temp
            print(self.brand, "AC", self.device_id, "temperature set to", self.temperature, "°C.")
        else:
            print("Temperature must be between 16 and 30 °C.")

class SmartCamera(SmartDevice):
    def __init__(self, device_id, brand, power_status = False, record_video = False):
        super().__init__(device_id, brand, power_status)
        self.record_video = record_video

    def start_recording(self):
        if self.power_status:
            self.record_video = True
            print(self.brand, "camera", self.device_id, "started recording.")
        else:
            print("Camera must be turned on to start recording.")

    def stop_recording(self):
        if self.record_video:
            self.record_video = False
            print(self.brand, "camera", self.device_id, "stopped recording.")
        else:
            print("Camera is not recording.")

Light = SmartLight("L001", "Philips")

Light.turn_on()
Light.set_brightness(75)

Fan = SmartFan("F001", "Dyson")
Fan.turn_on()
Fan.set_speed(2)

AC = SmartAC("AC001", "LG")
AC.turn_on()
AC.set_temperature(22)

Camera = SmartCamera("C001", "Sony")
Camera.turn_on()
Camera.start_recording()
Camera.stop_recording()