import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""
    
    def test_city_country(self):
        """Does a string like London, England work?"""
        london_england = city_country('London', 'England')
        self.assertEqual(london_england, 'London, England')
        
    def test_city_country_population(self):
        """Does a string like London, England, Population, 780000 work?"""
        location = city_country('Santiago', 'Chile', population=5000000)
        self.assertEqual(location, 'Santiago, Chile Population - 5000000')
        
unittest.main()