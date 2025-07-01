import tkinter as tk
from tkinter import messagebox
from app.weather_service import WeatherService
from app.exceptions import WeatherAPIError

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

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("App Clima IA")
        self.root.configure(bg="#117582")
        self.service = WeatherService()

        self.label = tk.Label(root, text="Previsão do Tempo com IA 🌍", font=("Tahoma", 18, "bold"), fg="#020c0d", bg="#117582")
        self.label.pack(pady=(15, 50))
        self.label2 = tk.Label(root, text="Digite o nome da cidade:", font=("Tahoma", 12, "bold"), fg="#020c0d", bg="#117582")
        self.label2.pack(pady=5)
        self.entry = tk.Text(root, width=50, height=3, font=("Tahoma", 12), fg="#020c0d", bg="#e6f2f3")
        self.entry.pack(pady=5)
        self.button = tk.Button(root, text="Obter Clima", command=self.get_weather, font=("Tahoma", 12, "bold"), bg="#18181a", fg="#e5e8e9", activebackground="#010607", activeforeground="#fff")
        self.button.pack(pady=5)
        self.result_frame = tk.Frame(root, bg="#e5e8e9", bd=2, relief="solid")
        self.result_frame.pack(pady=10, padx=30, fill="x")
        self.result_title = tk.Label(self.result_frame, text="Resultado ☀️", font=("Tahoma", 13, "bold"), fg="#020c0d", bg="#e5e8e9")
        self.result_title.pack(anchor="w", padx=10, pady=(8,0))
        self.result = tk.Label(self.result_frame, text="", font=("Tahoma", 12), justify="left", fg="#020c0d", bg="#e5e8e9")
        self.result.pack(anchor="w", padx=10, pady=(0,8))

    def get_weather(self):
        city = self.entry.get("1.0", "end").strip()
        if not city:
            messagebox.showwarning("Aviso", "Digite o nome de uma cidade.")
            return
        try:
            dados, cache = self.service.get_weather_for_city(city)
            temp = dados['current_weather']['temperature']
            wind = dados['current_weather']['windspeed']
            code = dados['current_weather']['weathercode']
            desc = weather_code_description(code)
            cidade_exib = dados.get('city_display', city.title())
            txt = (
                f"\n🌆  Cidade: "+cidade_exib+"\n"
                f"🌡️  Temperatura: {temp}°C\n"
                f"💨  Vento: {wind} km/h\n"
                f"☁️  Condição: {desc} {'(cache)' if cache else ''}"
            )
            self.result.config(text=txt)
        except WeatherAPIError as e:
            self.result.config(text=f"Erro: {e}")
        except Exception as e:
            self.result.config(text=f"Erro inesperado: {e}")

def main():
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
