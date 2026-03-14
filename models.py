# models.py

class Ambulance:
    def __init__(self):
        self.position = 0        # meters
        self.speed = 10          # m/sec (simulated)
        self.emergency = False

class TrafficSignal:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.state = "RED"       # RED or GREEN
        self.mode = "NORMAL"     # NORMAL or EVACUATION

class Road:
    def __init__(self):
        self.entry_blocked = False
        self.clear_lane = None   # LEFT or RIGHT
