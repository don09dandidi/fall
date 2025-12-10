from typing import Optional
from lab6.queue_implementations import Queue
from lab6.services import Dineable, Refuelable, Statistics
from lab6.car import Car


class CarStation:
    """Car service station with composition"""
    
    def __init__(self, 
                 dining_service: Optional[Dineable],
                 refueling_service: Refuelable,
                 queue: Queue[Car]):
        self.dining_service = dining_service
        self.refueling_service = refueling_service
        self.queue = queue
        self.stats = Statistics()   # ← acum funcționează
        
    def add_car(self, car: Car) -> None:
        """Add car to service queue"""
        self.queue.enqueue(car)
    
    def serve_cars(self) -> None:
        """Service all cars in queue"""
        while not self.queue.is_empty():
            car = self.queue.dequeue()
            if car is None:
                break
            
            # Serve dinner
            if car.is_dining and self.dining_service:
                self.dining_service.serve_dinner(str(car.id))
            elif not car.is_dining:
                self.stats.not_dining_count += 1
            
            # Refuel
            self.refueling_service.refuel(str(car.id), car.consumption)
