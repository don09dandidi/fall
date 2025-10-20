from trip import Trip

class Rider:
    def __init__(self, name):
        self.name = name
        self.total_distance = 0

    def start_trip(self, bicycle):
        print(f"🚴 {self.name} starts a trip with {bicycle.brand} bicycle.")
        return Trip(rider=self, bicycle=bicycle)

    def end_trip(self, trip):
        self.total_distance += trip.distance
        print(f"🏁 {self.name} finished the trip! Total distance now: {self.total_distance} km.")