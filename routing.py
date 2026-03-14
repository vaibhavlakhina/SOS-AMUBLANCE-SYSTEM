# routing.py

def choose_route(primary_clearable):
    """
    primary_clearable = True  → one-lane evacuation possible
    primary_clearable = False → reroute needed
    """
    if primary_clearable:
        print("🟢 Primary route selected (one-lane evacuation)")
        return "PRIMARY"
    else:
        print("🔁 Primary route failed, switching to SECONDARY route")
        return "SECONDARY"
