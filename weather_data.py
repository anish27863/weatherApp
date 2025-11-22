import requests
f=open("apikey.txt","r")
ak=f.read()
ak=ak[11:len(ak)-1]
class WeatherData:
    def __init__(self, api_key):
        if not api_key:
            raise ValueError("API key required")
        self.api_key = api_key
        self.main = {}
        self.weather_desc = ""
    
    def get_weather(city):
        api_key = ak 
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {'q': city, 'appid': api_key, 'units': 'metric'}
        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather_desc = data['weather'][0]['description']
            print(f"Weather in {city}: {weather_desc}")
            print(f"Temperature: {main['temp']}°C")
            print(f"Humidity: {main['humidity']}%")
            print(main)
            
        else:
            print(f"City {city} not found. Please check the name.")


    # city = input("Enter city name: ")
    # get_weather(city)
