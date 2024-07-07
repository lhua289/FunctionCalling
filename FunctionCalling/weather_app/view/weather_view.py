import tkinter as tk
from tkinter import messagebox

class WeatherAppView:
    def __init__(self, fetch_weather_callback):
        self.fetch_weather_callback = fetch_weather_callback

        self.root = tk.Tk()
        self.root.title("Weather Forecast App")

        self.city_label = tk.Label(self.root, text="Enter city name:")
        self.city_entry = tk.Entry(self.root)
        self.fetch_button = tk.Button(self.root, text="Fetch Weather", command=self.fetch_weather)

        self.weather_label = tk.Label(self.root, text="")
        self.temp_label = tk.Label(self.root, text="")
        self.humidity_label = tk.Label(self.root, text="")
        self.wind_label = tk.Label(self.root, text="")

        self.city_label.grid(row=0, column=0)
        self.city_entry.grid(row=0, column=1)
        self.fetch_button.grid(row=0, column=2)
        self.weather_label.grid(row=1, column=0, columnspan=3)
        self.temp_label.grid(row=2, column=0, columnspan=3)
        self.humidity_label.grid(row=3, column=0, columnspan=3)
        self.wind_label.grid(row=4, column=0, columnspan=3)

    def fetch_weather(self):
        city = self.city_entry.get()
        self.fetch_weather_callback(city)

    def update_weather_info(self, weather_data):
        if 'error' in weather_data:
            messagebox.showerror('Error', weather_data['error'])
        else:
            self.weather_label.config(text=f"Weather in {weather_data['city']}: {weather_data['weather']}")
            self.temp_label.config(text=f"Temperature: {weather_data['temperature']}°C")
            self.humidity_label.config(text=f"Humidity: {weather_data['humidity']}%")
            self.wind_label.config(text=f"Wind Speed: {weather_data['wind_speed']} m/s")

    def run(self):
        self.root.mainloop()