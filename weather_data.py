import requests


def read_apikey():
    '''Function to read API key from file'''
    with open("apikey.txt", "r") as f:
        return f.read().strip()[11:-1]

class WeatherData:
    def __init__(self, api_key=None):
        if not api_key:
            api_key = read_apikey()
        if not api_key:
            raise ValueError("API key required")
        self.api_key = api_key
        self.main = {}
        self.weather_desc = ""
        self.data = {}

    def get_weather(self, city):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            self.data = response.json()
            self.main = self.data['main']
            self.weather_desc = self.data['weather'][0]['description']
            return self.data
        else:
            return None
