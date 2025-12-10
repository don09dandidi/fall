from abc import ABC, abstractmethod


class Dineable(ABC):
    """Interface for dining services"""
    
    @abstractmethod
    def serve_dinner(self, car_id: str) -> None:
        """Serve dinner to passengers in car"""
        pass


class Refuelable(ABC):
    """Interface for refueling services"""
    
    @abstractmethod
    def refuel(self, car_id: str) -> None:
        """Refuel the car"""
        pass


# Global statistics tracker
class Statistics:
    """Singleton for tracking global statistics"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_stats()
        return cls._instance
    
    def _init_stats(self):
        self.electric_count = 0
        self.gas_count = 0
        self.people_count = 0
        self.robots_count = 0
        self.dining_count = 0
        self.not_dining_count = 0
        self.electric_consumption = 0
        self.gas_consumption = 0
    
    def reset(self):
        """Reset all statistics"""
        self._init_stats()
    
    def get_stats(self) -> dict:
        """Return statistics in required format"""
        return {
            "ELECTRIC": self.electric_count,
            "GAS": self.gas_count,
            "PEOPLE": self.people_count,
            "ROBOTS": self.robots_count,
            "DINING": self.dining_count,
            "NOT_DINING": self.not_dining_count,
            "CONSUMPTION": {
                "ELECTRIC": self.electric_consumption,
                "GAS": self.gas_consumption
            }
        }


class PeopleDinner(Dineable):
    """Dining service for people"""
    
    def __init__(self):
        self.stats = Statistics()
    
    def serve_dinner(self, car_id: str) -> None:
        print(f"Serving dinner to people in car {car_id}.")
        self.stats.people_count += 1
        self.stats.dining_count += 1


class RobotDinner(Dineable):
    """Dining service for robots"""
    
    def __init__(self):
        self.stats = Statistics()
    
    def serve_dinner(self, car_id: str) -> None:
        print(f"Serving dinner to robots in car {car_id}.")
        self.stats.robots_count += 1
        self.stats.dining_count += 1


class ElectricStation(Refuelable):
    """Refueling service for electric cars"""
    
    def __init__(self):
        self.stats = Statistics()
    
    def refuel(self, car_id: str, consumption: int = 0) -> None:
        print(f"Charging electric car {car_id}.")
        self.stats.electric_count += 1
        self.stats.electric_consumption += consumption


class GasStation(Refuelable):
    """Refueling service for gas cars"""
    
    def __init__(self):
        self.stats = Statistics()
    
    def refuel(self, car_id: str, consumption: int = 0) -> None:
        print(f"Refueling gas car {car_id}.")
        self.stats.gas_count += 1
        self.stats.gas_consumption += consumption