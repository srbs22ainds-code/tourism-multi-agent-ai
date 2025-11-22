from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent

weather_agent = WeatherAgent()
places_agent = PlacesAgent()

def tourism_ai_agent(city, want_weather, want_places):
    # Convert yes/no to boolean
    want_weather = want_weather.lower() == "yes"
    want_places = want_places.lower() == "yes"

    # If user didn't choose anything, default to places
    if not want_weather and not want_places:
        want_places = True

    weather_info = None
    places_info = None

    # Weather
    if want_weather:
        weather_info = weather_agent.get_weather_for_place(city)
        if weather_info is None:
            return "It doesn’t know this place exist."

    # Places
    if want_places:
        places_info = places_agent.get_places_for_place(city)
        if places_info is None:
            return "It doesn’t know this place exist."

    # Build response
    parts = []

    if weather_info:
        temp = weather_info["temperature"]
        rain = weather_info["rain_chance"]
        parts.append(f"In {city}, the temperature is {temp}°C with {rain}% chance of rain.")

    if places_info and places_info["places"]:
        parts.append("Places you can visit:")
        for p in places_info["places"]:
            parts.append("• " + p)
    elif places_info and not places_info["places"]:
        parts.append("I couldn't find tourist spots for this place.")

    return "\n".join(parts)


if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or type exit): ")
        if city.lower() in ["exit", "quit"]:
            break

        want_weather = input("Do you want weather information? (yes/no): ")
        want_places = input("Do you want tourist places? (yes/no): ")

        result = tourism_ai_agent(city, want_weather, want_places)
        print("\nAI:", result)
