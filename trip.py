from datetime import datetime

class Trip:
    def __init__(self, rider, bicycle):
        self.rider = rider
        self.bicycle = bicycle
        self.start_time = datetime.now()
        self.distance = 0
        print(f"🕒 Trip started at {self.start_time.strftime('%H:%M:%S')}")

    def record_distance(self, km):
        self.distance += km
        print(f"📏 Trip updated: {self.distance} km traveled so far.")

    def end(self):
        self.end_time = datetime.now()
        duration = (self.end_time - self.start_time).seconds
        print(f"✅ Trip ended at {self.end_time.strftime('%H:%M:%S')} (Duration: {duration} sec)")
