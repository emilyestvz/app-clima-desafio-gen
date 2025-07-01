import time

from .weather_api import WeatherAPI
from .geocoding_api import GeocodingAPI
from .exceptions import WeatherAPIError

class WeatherService:
    """Classe de serviço para lógica de negócio e cache."""
    def __init__(self):
        self.api = WeatherAPI()
        self.geocoding = GeocodingAPI()
        self.cache = {}
        self.cache_expiry = 300  # segundos

    def get_weather_for_city(self, city, lat=None, lon=None):
        city = city.strip()
        now = time.time()
        if city.lower() in self.cache and now - self.cache[city.lower()]['timestamp'] < self.cache_expiry:
            return self.cache[city.lower()]['data'], True
        # Busca coordenadas via API de geocodificação se não fornecido
        if lat is None or lon is None:
            results = self.geocoding.get_coordinates(city)
            if len(results) > 1:
                # Retorna lista de opções para o frontend
                return {"opcoes": results}, False
            r = results[0]
            lat, lon = r["latitude"], r["longitude"]
            nome_oficial = r["name"]
            estado = r.get("admin1", "")
            pais = r.get("country", "")
        else:
            nome_oficial = city
            estado = ""
            pais = ""
        data = self.api.get_weather(lat, lon)
        self.cache[city.lower()] = {'data': data, 'timestamp': now}
        # Adiciona nome oficial, estado e país ao retorno para exibir na interface
        data['city_display'] = f"{nome_oficial}, {estado}, {pais}".strip(', ')
        return data, False
