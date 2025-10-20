class Bicycle:
    def __init__(self, brand, gear_count):
        self.brand = brand
        self.gear_count = gear_count
        self.current_speed = 0
        self.current_gear = 1

    def pedal(self):
        self.current_speed += 2
        print(f"🚴‍♂️ Pedaling... Speed increased to {self.current_speed} km/h")

    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 2
        print(f"🛑 Braking... Speed decreased to {self.current_speed} km/h")

    def change_gear(self, new_gear):
        if 1 <= new_gear <= self.gear_count:
            self.current_gear = new_gear
            print(f"⚙️ Changed to gear {self.current_gear}")
        else:
            print("❌ Invalid gear number!")
