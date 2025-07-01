# Pequeno dicionário de cidades para exemplo. Em produção, use uma base maior ou API de geolocalização.
CITY_COORDINATES = {
    "sao paulo": (-23.5505, -46.6333),
    "rio de janeiro": (-22.9068, -43.1729),
    "brasilia": (-15.7939, -47.8828),
    "belo horizonte": (-19.9167, -43.9345),
    "curitiba": (-25.4284, -49.2733),
    "porto alegre": (-30.0346, -51.2177),
    "recife": (-8.0476, -34.8770),
    "salvador": (-12.9777, -38.5016),
    "fortaleza": (-3.7172, -38.5433),
    "manaus": (-3.1190, -60.0217)
}

def get_city_coordinates(city):
    return CITY_COORDINATES.get(city)
