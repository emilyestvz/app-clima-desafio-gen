import requests
from .exceptions import WeatherAPIError

class GeocodingAPI:
    """Classe para buscar coordenadas de uma cidade usando a API Open-Meteo."""
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"

    def get_coordinates(self, city_name, count=5):
        params = {"name": city_name, "count": count, "language": "pt", "format": "json"}
        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data.get("results"):
                # Retorna lista de resultados (cidade, estado, país, lat, lon)
                return [
                    {
                        "name": r["name"],
                        "admin1": r.get("admin1", ""),
                        "country": r.get("country", ""),
                        "latitude": r["latitude"],
                        "longitude": r["longitude"]
                    } for r in data["results"]
                ]
            else:
                raise WeatherAPIError("Cidade não encontrada na API de geocodificação.")
        except requests.RequestException as e:
            raise WeatherAPIError(f"Erro ao buscar coordenadas: {e}")
