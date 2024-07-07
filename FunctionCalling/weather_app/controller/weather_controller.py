import sys
sys.path.append('/Users/lhua/FunctionCalling')

from weather_app.model.weather_model import get_weather
from weather_app.view.weather_view import WeatherAppView

class WeatherController:
    def __init__(self, api_key):
        self.api_key = api_key
        self.view = WeatherAppView(self.fetch_weather)

    def fetch_weather(self, city):
        weather_data = get_weather(self.api_key, city)
        self.view.update_weather_info(weather_data)

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '6ea760875302d7ea5df93544a983c2e3'
    controller = WeatherController(api_key)
    controller.view.run()