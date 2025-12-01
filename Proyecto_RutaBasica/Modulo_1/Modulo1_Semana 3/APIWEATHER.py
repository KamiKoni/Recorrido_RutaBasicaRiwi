import requests

def obtener_clima(ciudad):
    api_key = "14bb98ea8115bbd500c1b7398b14a465"
    url_completa = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={ciudad}&appid={api_key}&units=metric&lang=es"
    )

    respuesta = requests.get(url_completa)
    datos = respuesta.json()

    if datos["cod"] != 404:
        clima_actual = datos["main"]
        temperatura_actual = clima_actual["temp"]
        sensacion_termica = clima_actual["feels_like"]
        humedad = clima_actual["humidity"]
        descripcion_clima = datos["weather"][0]["description"]

        print(f"Clima en {ciudad}:")
        print(f"  Temperatura: {temperatura_actual}°C")
        print(f"  Sensación térmica: {sensacion_termica}°C")
        print(f"  Humedad: {humedad}%")
        print(f"  Descripción: {descripcion_clima}")
    else:
        print(f"No se encontró información para la ciudad: {ciudad}")

ciudad = input("Introduce el nombre de la ciudad: ")
obtener_clima(ciudad)
