class TestSemaphore(unittest.TestCase):
    """Test Semaphore car routing"""
    
    def setUp(self):
        Statistics().reset()
        self.semaphore = create_stations()
    
    def test_routes_gas_cars_correctly(self):
        """Test gas cars go to gas stations"""
        cars = [
            Car(1, "GAS", "PEOPLE", True, 30),
            Car(2, "GAS", "PEOPLE", False, 40),
            Car(3, "GAS", "ROBOTS", True, 35)
        ]
        
        self.semaphore.route_cars(cars)
        self.semaphore.serve_all()
        
        stats = Statistics()
        self.assertEqual(stats.gas_count, 3)
        self.assertEqual(stats.gas_consumption, 105)
    
    def test_routes_electric_cars_correctly(self):
        """Test electric cars go to electric stations"""
        cars = [
            Car(1, "ELECTRIC", "PEOPLE", False, 25),
            Car(2, "ELECTRIC", "ROBOTS", True, 30)
        ]
        
        self.semaphore.route_cars(cars)
        self.semaphore.serve_all()
        
        stats = Statistics()
        self.assertEqual(stats.electric_count, 2)
        self.assertEqual(stats.electric_consumption, 55)
    
    def test_complete_statistics(self):
        """Test complete statistics match expected"""
        cars = [
            Car(1, "ELECTRIC", "PEOPLE", False, 42),
            Car(2, "ELECTRIC", "PEOPLE", False, 26),
            Car(3, "GAS", "ROBOTS", True, 41)
        ]
        
        self.semaphore.route_cars(cars)
        self.semaphore.serve_all()
        
        expected = {
            "ELECTRIC": 2,
            "GAS": 1,
            "PEOPLE": 2,
            "ROBOTS": 1,
            "DINING": 1,
            "NOT_DINING": 2,
            "CONSUMPTION": {
                "ELECTRIC": 68,
                "GAS": 41
            }
        }
        
        stats = self.semaphore.get_statistics()
        self.assertEqual(stats, expected)


# Run tests
if __name__ == "__main__":
    unittest.main()