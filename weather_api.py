import requests

def weather_icons(icon):
    weather_icons = {
        "01d": "☀️",  # Clear sky (day)
        "01n": "🌙",  # Clear sky (night)
        "02d": "⛅",  # Few clouds (day)
        "02n": "🌙⛅",  # Few clouds (night)
        "03d": "🌥️",  # Scattered clouds (day)
        "03n": "🌥️",  # Scattered clouds (night)
        "04d": "☁️",  # Broken clouds (day)
        "04n": "☁️",  # Broken clouds (night)
        "09d": "🌧️",  # Shower rain (day)
        "09n": "🌧️",  # Shower rain (night)
        "10d": "🌧️",  # Rain (day)
        "10n": "🌧️",  # Rain (night)
        "11d": "⛈️",  # Thunderstorm (day)
        "11n": "⛈️",  # Thunderstorm (night)
        "13d": "❄️",  # Snow (day)
        "13n": "❄️",  # Snow (night)
        "50d": "🌫️",  # Mist/fog (day)
        "50n": "🌫️"   # Mist/fog (night)
    }
    for key,val in weather_icons.items():
        if icon == key:
            return val
    else:
        return None

def weather_api(url):
    response = requests.get(url)
    data = response.json()
    if data['cod']==200:
        return data
    else:
        return {}

def main():
    api_key = 'your api key from api.openweathermap.org'
    city_name = input('country name to search: ')
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
    weather_data = weather_api(url)
    if len(weather_data)>0:
        weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        icon = weather_icons(weather_data['weather'][0]['icon'])
        temp = round((5/9)* (weather_data['main']['temp'] - 32) - 100,2)
        cent = u'\N{DEGREE SIGN}'
        print(f"Weather : {weather} {icon}\nDescription : {description}\nTemperature : {temp} {cent}C")
    else:
        print('api not found')

main()