# map_data.py

def get_road_width(road_type, lanes=None):
    """
    Estimate road width using map data
    """
    if lanes:
        return lanes * 3.5  # meters per lane (standard)

    road_width_map = {
        "primary": 9,
        "secondary": 7,
        "residential": 5
    }

    return road_width_map.get(road_type, 5)
