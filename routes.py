# routes.py

from map_data import get_road_width

AMBULANCE_SPEED = 12      # m/s (~43 km/h)
SIGNAL_DELAY = 20         # seconds per signal


class Route:
    def __init__(self, name, road_type, lanes, signals, distance):
        self.name = name
        self.road_type = road_type
        self.lanes = lanes
        self.signals = signals
        self.distance = distance  # meters


def estimate_time(route):
    travel_time = route.distance / AMBULANCE_SPEED
    signal_time = route.signals * SIGNAL_DELAY
    return travel_time + signal_time


def evaluate_route(route):
    width = get_road_width(route.road_type, route.lanes)
    time_required = estimate_time(route)

    score = 0

    # Width importance
    if width >= 6:
        score += 5
    else:
        score -= 5

    # Time importance (lower time = better)
    score -= time_required / 60   # convert to minutes

    return score, width, time_required


def select_best_route(routes):
    best_route = None
    best_score = -9999

    print("\n📊 Evaluating possible routes (time-aware):\n")

    for route in routes:
        score, width, time_required = evaluate_route(route)

        print(
            f"🛣️ {route.name} | width: {width}m | "
            f"signals: {route.signals} | "
            f"time: {int(time_required)} sec | "
            f"score: {round(score,2)}"
        )

        if score > best_score:
            best_score = score
            best_route = route

    return best_route
