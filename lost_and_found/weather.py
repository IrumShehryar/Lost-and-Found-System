import requests

class Weather:
    API_KEY = "8b4b83d8e204304ee69faad92696fbfb"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_current_weather(location: str) -> str:
        """
        Get the current weather for a given location using OpenWeatherMap API.
        """
        params = {
            "q": location,
            "appid": Weather.API_KEY,
            "units": "metric"
        }
        try:
            response = requests.get(Weather.BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"{temperature}°C, {description}"
        except Exception as e:
            return f"Weather not available: {e}"




