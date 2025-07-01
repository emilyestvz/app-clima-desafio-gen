from app.weather_service import WeatherService
from app.exceptions import WeatherAPIError

def main():
    print("\n=== Previsão do Tempo ===")
    service = WeatherService()
    while True:
        cidades = input("Digite o nome das cidades separadas por vírgula (ou 'sair'): ")
        if cidades.strip().lower() == 'sair':
            break
        for cidade in cidades.split(','):
            cidade = cidade.strip()
            if not cidade:
                continue
            try:
                dados, cache = service.get_weather_for_city(cidade)
                temp = dados['current_weather']['temperature']
                wind = dados['current_weather']['windspeed']
                code = dados['current_weather']['weathercode']
                desc = weather_code_description(code)
                cidade_exib = dados.get('city_display', cidade.title())
                print(f"\nCidade: {cidade_exib} | Temperatura: {temp}°C | Vento: {wind} km/h | Condição: {desc} {'(cache)' if cache else ''}")
            except WeatherAPIError as e:
                print(f"Erro para {cidade.title()}: {e}")
            except Exception as e:
                print(f"Erro inesperado para {cidade.title()}: {e}")
    print("\nAté logo!")

# Descrição simplificada dos códigos de tempo da Open-Meteo
def weather_code_description(code):
    code_map = {
        0: "Céu limpo",
        1: "Principalmente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Névoa",
        48: "Névoa gelada",
        51: "Garoa leve",
        53: "Garoa moderada",
        55: "Garoa densa",
        61: "Chuva leve",
        63: "Chuva moderada",
        65: "Chuva forte",
        71: "Neve leve",
        73: "Neve moderada",
        75: "Neve forte",
        80: "Aguaceiro leve",
        81: "Aguaceiro moderado",
        82: "Aguaceiro forte",
        95: "Trovoada",
        96: "Trovoada com granizo leve",
        99: "Trovoada com granizo forte"
    }
    return code_map.get(code, "Desconhecido")

if __name__ == "__main__":
    main()
