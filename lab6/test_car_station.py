class TestCarStation(unittest.TestCase):
    """Test CarStation composition"""
    
    def setUp(self):
        Statistics().reset()
    
    def test_car_station_serves_with_dining(self):
        """Test CarStation serves cars with dining"""
        station = CarStation(
            PeopleDinner(),
            ElectricStation(),
            ArrayQueue()
        )
        
        car1 = Car(1, "ELECTRIC", "PEOPLE", True, 25)
        car2 = Car(2, "ELECTRIC", "PEOPLE", True, 30)
        
        station.add_car(car1)
        station.add_car(car2)
        
        station.serve_cars()
        
        stats = Statistics()
        self.assertEqual(stats.electric_count, 2)
        self.assertEqual(stats.people_count, 2)
        self.assertEqual(stats.dining_count, 2)
    
    def test_car_station_no_dining(self):
        """Test CarStation handles cars without dining"""
        station = CarStation(
            None,  # No dining service
            GasStation(),
            LinkedQueue()
        )
        
        car = Car(1, "GAS", "PEOPLE", False, 40)
        station.add_car(car)
        station.serve_cars()
        
        stats = Statistics()
        self.assertEqual(stats.gas_count, 1)
        self.assertEqual(stats.not_dining_count, 1)
