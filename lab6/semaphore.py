from typing import List, Dict
from lab6.car import Car
from lab6.car_station import CarStation
from lab6.services import Statistics


class Semaphore:
    """Routes cars to appropriate CarStation"""

    def __init__(self):
        self.stations: Dict[tuple, CarStation] = {}
        self.stats = Statistics()

    def register_station(self, car_type: str, passenger_type: str,
                         station: CarStation) -> None:
        """Register a car station for specific car and passenger types"""
        key = (car_type, passenger_type)
        self.stations[key] = station

    def route_car(self, car: Car) -> None:
        """Route car to appropriate station"""
        key = (car.type, car.passengers)

        if key not in self.stations:
            print(f"Warning: No station available for {car.type} car with {car.passengers}")
            return

        station = self.stations[key]
        station.add_car(car)

    def route_cars(self, cars: List[Car]) -> None:
        """Route multiple cars"""
        for car in cars:
            self.route_car(car)

    def serve_all(self) -> None:
        """Serve cars at all stations"""
        for station in self.stations.values():
            station.serve_cars()

    def get_statistics(self) -> dict:
        """Get final statistics"""
        return self.stats.get_stats()
