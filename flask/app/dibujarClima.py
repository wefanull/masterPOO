import requests
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

def consulta_clima(ciudad):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    api_key = "7704f1b7c788fd5284e7b222ff5bdbd3"
    params = {
        'q': ciudad,
        'appid': api_key,
        'units': 'metric',
        'lang': 'es'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        return {
            'ciudad': weather_data['name'],
            'temperatura': weather_data['main']['temp'],
            'icono': weather_data['weather'][0]['icon'],
            'descripcion': weather_data['weather'][0]['description']
        }
    else:
        raise Exception(f"Error al consultar la API de OpenWeather: {response.status_code}")

def genera_imagen(ciudad):
    try:
        datos_clima = consulta_clima(ciudad)
        icon_code = datos_clima['icono']

        if icon_code.endswith('d'):
            fondo = Color('#4193EE')
        else:
            fondo = Color('#4A6380')

        with Drawing() as draw:
            draw.stroke_color = Color('black')
            draw.stroke_width = 2
            draw.fill_color = Color('white')

            if icon_code in ['01d', '01n']:  # Cielo despejado
                draw.fill_color = Color('#F8DF80')
                draw.circle((400, 300), (500, 300))  # Círculo centrado
            elif icon_code in ['02d', '02n']:  # Pocas nubes
                draw.fill_color = Color('white')
                draw.rectangle(left=300, top=200, right=500, bottom=400)  # Rectángulo centrado
            elif icon_code in ['03d', '03n', '04d', '04n']:  # Nubes dispersas
                draw.fill_color = Color('#9E9E9D')
                draw.ellipse((400, 300), (150, 100))  # Elipse centrada
            elif icon_code in ['09d', '09n']:  # Llovizna
                draw.stroke_color = Color('#9997E0')
                draw.line((250, 300), (550, 300))  # Línea horizontal centrada
            elif icon_code in ['10d', '10n']:  # Lluvia ligera
                draw.stroke_color = Color('#72BDD3')
                draw.line((300, 200), (500, 400))  # Línea diagonal centrada
            elif icon_code in ['11d', '11n']:  # Tormenta eléctrica
                draw.fill_color = Color('purple')
                draw.polygon([(350, 350), (400, 200), (450, 350)])  # Triángulo centrado
            elif icon_code in ['13d', '13n']:  # Nieve
                draw.stroke_color = Color('white')
                draw.arc((300, 200), (500, 400), 0, 360)  # Arco centrado
            elif icon_code in ['50d', '50n']:  # Niebla
                draw.stroke_color = Color('#566063')
                draw.bezier([(250, 300), (350, 200), (450, 400), (550, 300)])  # Curva Bézier centrada
            else:
                draw.text(350, 300, "Icono desconocido")

            with Image(width=800, height=600, background=fondo) as image:
                draw.font = 'fonts/WinkySans.ttf'
                draw.fill_color = Color('white')
                draw.stroke_color = Color('Black')
                draw.font_size = 50
                draw.text(50, 100, f"{datos_clima['ciudad']}")
                draw.text(600, 550, f"{datos_clima['temperatura']}°C")
                draw.text(50, 550, f"{datos_clima['descripcion'].capitalize()}")
                draw(image)
                image.format = 'png'
                return image.make_blob()
    except Exception as e:
        with Image(width=800, height=600, background=Color('gray')) as image:
            with Drawing() as draw:
                draw.font = 'fonts/WinkySans.ttf'
                draw.fill_color = Color('white')
                draw.font_size = 40
                draw.text(50, 300, f"Error: {str(e)}")
                draw(image)
                image.format = 'png'
                return image.make_blob()