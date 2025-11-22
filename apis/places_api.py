import requests

def get_tourist_places(lat: float, lon: float, max_places: int = 5):
    url = "https://overpass-api.de/api/interpreter"

    overpass_query = f"""
    [out:json];
    (
      node["tourism"~"attraction|museum|zoo|theme_park"](around:10000,{lat},{lon});
    );
    out body {max_places};
    """

    response = requests.post(url, data={"data": overpass_query}, timeout=25)
    response.raise_for_status()
    data = response.json()

    elements = data.get("elements", [])
    places = []
    for e in elements:
        name = e.get("tags", {}).get("name")
        if name:
            places.append(name)

    # Ensure unique names and limit list length
    unique_places = list(dict.fromkeys(places))[:max_places]
    return unique_places
