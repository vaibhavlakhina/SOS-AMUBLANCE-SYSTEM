from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(".", "map.html")

@app.route("/hospitals")
def hospitals():
    return jsonify([
        {"name": "AIIMS Delhi", "lat": 28.5672, "lon": 77.2100},
        {"name": "Safdarjung Hospital", "lat": 28.5677, "lon": 77.2066},
        {"name": "RML Hospital", "lat": 28.6248, "lon": 77.2021},
        {"name": "Fortis Noida", "lat": 28.5673, "lon": 77.3210},
        {"name": "Kailash Hospital Noida", "lat": 28.5354, "lon": 77.3910},
    ])

if __name__ == "__main__":
    app.run(debug=True, port=5001)
