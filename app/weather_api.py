import requests
from .exceptions import WeatherAPIError

class WeatherAPI:
    """Classe responsável por interagir com a API Open-Meteo."""
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def get_weather(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "hourly": "temperature_2m,precipitation,weathercode,wind_speed_10m"
        }
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise WeatherAPIError(f"Erro ao acessar a API: {e}")
