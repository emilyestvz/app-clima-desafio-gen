from flask import Flask, render_template, request, jsonify
from app.weather_service import WeatherService
from app.exceptions import WeatherAPIError

def create_app():
    app = Flask(__name__)
    service = WeatherService()

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/clima", methods=["POST"])
    def clima():
        cidade = request.json.get("cidade", "").strip()
        if not cidade:
            return jsonify({"erro": "Digite o nome de uma cidade."}), 400
        try:
            lat = request.json.get("lat")
            lon = request.json.get("lon")
            if lat is not None and lon is not None:
                lat = float(lat)
                lon = float(lon)
                dados, cache = service.get_weather_for_city(cidade, lat=lat, lon=lon)
            else:
                dados, cache = service.get_weather_for_city(cidade)
                # Se vier opções, envie para o frontend
                if isinstance(dados, dict) and "opcoes" in dados:
                    return jsonify({"opcoes": dados["opcoes"]}), 200
            temp = float(dados['current_weather']['temperature'])
            wind = float(dados['current_weather']['windspeed'])
            code = dados['current_weather']['weathercode']
            desc = weather_code_description(code)
            cidade_exib = dados.get('city_display', cidade.title())
            return jsonify({
                "cidade": cidade_exib,
                "temperatura": f"{temp:.1f}",
                "vento": f"{wind:.1f}",
                "condicao": desc,
                "cache": cache
            })
        except WeatherAPIError as e:
            return jsonify({"erro": str(e)}), 400
        except Exception as e:
            return jsonify({"erro": f"Erro inesperado: {e}"}), 500

    return app

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
    app = create_app()
    app.run(debug=True)
