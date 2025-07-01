import unittest
from app.weather_service import WeatherService
from app.exceptions import WeatherAPIError

class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.service = WeatherService()

    def test_city_not_found(self):
        with self.assertRaises(WeatherAPIError):
            self.service.get_weather_for_city("cidadeinexistente")

    def test_cache(self):
        # Testa se o cache funciona para uma cidade conhecida
        data1, cache1 = self.service.get_weather_for_city("sao paulo")
        data2, cache2 = self.service.get_weather_for_city("sao paulo")
        self.assertEqual(data1, data2)
        self.assertFalse(cache1)
        self.assertTrue(cache2)

if __name__ == "__main__":
    unittest.main()
