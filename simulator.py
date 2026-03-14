# simulator.py

def evacuation_possible(road_width):
    """
    Check if one-lane evacuation is possible
    """
    if road_width < 6:   # meters (narrow road)
        print("❌ Road too narrow for one-lane evacuation")
        return False
    print("✅ Road wide enough for one-lane evacuation")
    return True


def move_ambulance(ambulance, signals):
    """
    Move ambulance forward and activate signals sequentially
    """
    ambulance.position += ambulance.speed
    print(f"🚑 Ambulance position: {ambulance.position} m")

    # Sequential signal control (forward flush)
    for signal in signals:
        if ambulance.position < signal.position:
            signal.state = "GREEN"
            print(f"🟢 Signal {signal.name} turned GREEN (evacuating traffic)")
            break
