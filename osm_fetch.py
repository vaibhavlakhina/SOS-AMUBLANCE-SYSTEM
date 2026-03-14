import requests

def fetch_road_data(lat, lon):
    query = f"""
    [out:json];
    way(around:50,{lat},{lon})["highway"];
    out tags;
    """
    url = "http://overpass-api.de/api/interpreter"
    response = requests.post(url, data=query)
    data = response.json()

    if len(data["elements"]) == 0:
        return None

    road = data["elements"][0]["tags"]
    return {
        "road_type": road.get("highway", "unknown"),
        "lanes": int(road.get("lanes", 1))
    }
