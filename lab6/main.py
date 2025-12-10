from lab6.semaphore import Semaphore
from lab6.car_station import CarStation
from lab6.services import (
    Statistics,
    PeopleDinner,
    RobotDinner,
    ElectricStation,
    GasStation
)
from lab6.queue_implementations import (
    ArrayQueue,
    LinkedQueue,
    CircularQueue
)
from lab6.car import Car
import json
import os
from typing import List


def create_stations() -> Semaphore:
    """Create all possible car station combinations"""
    semaphore = Semaphore()
    
    # Electric + People + Dining
    semaphore.register_station(
        "ELECTRIC", "PEOPLE",
        CarStation(PeopleDinner(), ElectricStation(), LinkedQueue())
    )
    
    # Electric + Robots + Dining
    semaphore.register_station(
        "ELECTRIC", "ROBOTS",
        CarStation(RobotDinner(), ElectricStation(), LinkedQueue())
    )
    
    # Gas + People + Dining
    semaphore.register_station(
        "GAS", "PEOPLE",
        CarStation(PeopleDinner(), GasStation(), ArrayQueue())
    )
    
    # Gas + Robots + Dining
    semaphore.register_station(
        "GAS", "ROBOTS",
        CarStation(RobotDinner(), GasStation(), CircularQueue())
    )
    
    return semaphore


def load_cars_from_json(filepath: str) -> List[Car]:
    """Load cars from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return [Car.from_dict(car_data) for car_data in data]


def main():
    """Main application entry point"""
    # Reset statistics
    Statistics().reset()
    
    # Create semaphore and stations
    semaphore = create_stations()
    
    # Load cars (synchronous version)
    cars_file = os.path.join("lab6", "cars.json")

    
    if not os.path.exists(cars_file):
        print(f"Error: {cars_file} not found!")
        print("Please run the generator script first.")
        return
    
    # Load and route cars
    cars = load_cars_from_json(cars_file)
    print(f"Loaded {len(cars)} cars from {cars_file}")
    print("-" * 50)
    
    semaphore.route_cars(cars)
    
    # Serve all cars
    print("\nServicing cars...")
    print("-" * 50)
    semaphore.serve_all()
    
    # Print statistics
    print("\n" + "=" * 50)
    print("STATISTICS")
    print("=" * 50)
    stats = semaphore.get_statistics()
    print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()