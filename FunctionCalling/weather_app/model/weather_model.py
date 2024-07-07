import requests

def get_weather(api_key, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx errors
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return {
            'city': city,
            'weather': weather_description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}