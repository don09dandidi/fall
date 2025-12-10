class TestServices(unittest.TestCase):
    """Test dining and refueling services"""
    
    def setUp(self):
        """Reset statistics before each test"""
        Statistics().reset()
    
    def test_people_dinner_tracking(self):
        """Test PeopleDinner tracks correctly"""
        dinner = PeopleDinner()
        stats = Statistics()
        
        dinner.serve_dinner("1")
        dinner.serve_dinner("2")
        
        self.assertEqual(stats.people_count, 2)
        self.assertEqual(stats.dining_count, 2)
    
    def test_electric_station_consumption(self):
        """Test ElectricStation tracks consumption"""
        station = ElectricStation()
        stats = Statistics()
        
        station.refuel("1", 25)
        station.refuel("2", 35)
        
        self.assertEqual(stats.electric_count, 2)
        self.assertEqual(stats.electric_consumption, 60)
    
    def test_multiple_stations_same_type(self):
        """Test multiple stations share statistics"""
        station1 = ElectricStation()
        station2 = ElectricStation()
        stats = Statistics()
        
        station1.refuel("1", 10)
        station2.refuel("2", 20)
        
        # Should count as one pool
        self.assertEqual(stats.electric_count, 2)
        self.assertEqual(stats.electric_consumption, 30)
