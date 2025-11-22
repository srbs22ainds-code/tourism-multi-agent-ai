from apis.geocoding_api import geocode_place
from apis.weather_api import get_weather

class WeatherAgent:
    def get_weather_for_place(self, place_name: str):
        location = geocode_place(place_name)
        if not location:
            return None  # Parent will handle unknown place
        weather = get_weather(location["lat"], location["lon"])
        return {
            "place_name": place_name,
            "display_name": location["display_name"],
            "temperature": weather["temperature"],
            "rain_chance": weather["rain_chance"]
        }
