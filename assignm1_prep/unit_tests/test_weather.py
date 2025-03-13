import unittest
from weather import get_temperature

class WeatherTest(unittest.TestCase):
    def test_get_temperature_1(self):
        self.assertEqual(get_temperature("London"), 26)

    def test_get_temperature_2(self):
        self.assertEqual(get_temperature("Luxembourg"), "Unknown")

if __name__ == "__main__":
    unittest.main()