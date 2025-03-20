import requests
import os
#from dotenv import load_dotenv


class Clima:
    def __init__(self):
        #load_dotenv()
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.api_key = "7704f1b7c788fd5284e7b222ff5bdbd3" #os.getenv('API_KEY')

    def consulta_ciudad(self,ciudad):
        params = {
            'q': ciudad,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()
    
    def extrae_relevantes(self,ciudad):
        weather_data=self.consulta_ciudad(ciudad)
        return {
            'ciudad': weather_data['name'],
            'temperatura': weather_data['main']['temp'],
            'icono': weather_data['weather'][0]['icon'],
            'description': weather_data['weather'][0]['description']
        }

c=Clima()

print(c.extrae_relevantes('Toluca'))