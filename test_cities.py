import unittest
import city_functions


class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        result= city_functions.place('ktm','nepal')
        self.assertEqual(result, 'ktm,nepal')


if __name__=='__main__':
    unittest.main()
