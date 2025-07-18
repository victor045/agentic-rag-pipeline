# tool_weather.py

from langchain.tools import tool
import requests
import os

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"

@tool
def get_weather(city: str, units: str = "metric") -> str:
    """Get current weather for a given city using OpenWeatherMap."""
    if not WEATHER_API_KEY:
        return "❌ Weather API key not set."

    try:
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": units,
            "lang": "en"
        }
        response = requests.get(WEATHER_API_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return f"⚠️ Error: {data.get('message', 'Unknown error')}"

        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"🌤️ Weather in {city.title()}: {weather}, {temp}°{('C' if units == 'metric' else 'F')}"

    except Exception as e:
        return f"❌ Failed to fetch weather: {str(e)}"


# Export tool
weather_tools = [get_weather]

