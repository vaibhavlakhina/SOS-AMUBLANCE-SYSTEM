# controller.py

def start_evacuation(road, signals):
    print("\n🚨 EVACUATION MODE ACTIVATED")
    road.entry_blocked = True

    # Police enforces one-lane clearance
    road.clear_lane = "RIGHT"   # RIGHT lane for ambulance
    print("🚓 Police enforcing ONE-LANE clearance on RIGHT side")

    # Start with all signals RED
    for signal in signals:
        signal.mode = "EVACUATION"
        signal.state = "RED"


def end_evacuation(road, signals):
    print("\n✅ EVACUATION MODE ENDED")
    road.entry_blocked = False
    road.clear_lane = None

    for signal in signals:
        signal.mode = "NORMAL"
        signal.state = "RED"
