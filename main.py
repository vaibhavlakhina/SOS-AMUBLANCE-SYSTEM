# main.py

from models import Ambulance, TrafficSignal, Road
from controller import start_evacuation, end_evacuation
from simulator import move_ambulance, evacuation_possible
from routing import choose_route
from osm_fetch import fetch_road_data
from routes import Route, select_best_route, estimate_time
import time

# -----------------------------------
# Create core objects
# -----------------------------------
ambulance = Ambulance()
road = Road()

signals = [
    TrafficSignal("S1", 100),
    TrafficSignal("S2", 300),
    TrafficSignal("S3", 600)
]

# -----------------------------------
# Emergency trigger
# -----------------------------------
ambulance.emergency = True
print("🚑 Emergency received from ambulance")

# -----------------------------------
# Ambulance GPS (entry point)
# -----------------------------------
lat, lon = 28.6139, 77.2090
print(f"📍 Ambulance entry GPS: ({lat}, {lon})")

# -----------------------------------
# Fetch entry road from OpenStreetMap
# -----------------------------------
try:
    road_info = fetch_road_data(lat, lon)
except Exception:
    road_info = None

if road_info:
    entry_road_type = road_info["road_type"]
    entry_lanes = road_info["lanes"]
    print(f"🛣️ Entry road detected: {entry_road_type}, lanes: {entry_lanes}")
else:
    entry_road_type = "residential"
    entry_lanes = 1
    print("⚠️ Entry road not detected, using fallback")

# -----------------------------------
# MULTI-ROUTE OPTIONS
# -----------------------------------
route_A = Route(
    "Route A (Entry Road)",
    entry_road_type,
    entry_lanes,
    signals=3,
    distance=600
)

route_B = Route(
    "Route B",
    "secondary",
    lanes=2,
    signals=2,
    distance=750
)

route_C = Route(
    "Route C",
    "primary",
    lanes=2,
    signals=5,
    distance=500
)

routes = [route_A, route_B, route_C]

# -----------------------------------
# Select best route (TIME-BASED)
# -----------------------------------
best_route = select_best_route(routes)

print(f"\n✅ Best route selected: {best_route.name}")

# -----------------------------------
# Estimated arrival time
# -----------------------------------
arrival_time = estimate_time(best_route)
print(f"⏱️ Estimated arrival time: {int(arrival_time)} seconds")

# -----------------------------------
# Feasibility check (width-based)
# -----------------------------------
from map_data import get_road_width

selected_width = get_road_width(best_route.road_type, best_route.lanes)
can_clear = evacuation_possible(selected_width)
route_decision = choose_route(can_clear)

if route_decision == "SECONDARY":
    print("🚑 Ambulance rerouted via alternate road")
    exit()

# -----------------------------------
# Start evacuation
# -----------------------------------
start_evacuation(road, signals)

# -----------------------------------
# Simulate ambulance movement
# -----------------------------------
while ambulance.position < 700:
    move_ambulance(ambulance, signals)
    time.sleep(1)

# -----------------------------------
# End evacuation
# -----------------------------------
ambulance.emergency = False
end_evacuation(road, signals)
