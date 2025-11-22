from apis.geocoding_api import geocode_place
from apis.places_api import get_tourist_places

class PlacesAgent:
    def get_places_for_place(self, place_name: str, max_places: int = 5):
        location = geocode_place(place_name)
        if not location:
            return None
        places = get_tourist_places(location["lat"], location["lon"], max_places=max_places)
        return {
            "place_name": place_name,
            "display_name": location["display_name"],
            "places": places
        }
