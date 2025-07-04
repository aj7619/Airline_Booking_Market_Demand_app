from flask import Flask, render_template, request, jsonify
from processor import simulate_demand
import random

app = Flask(__name__)

def get_popular_routes():
    routes = [
        ("SYD", "MEL"),
        ("BNE", "SYD"),
        ("ADL", "PER"),
        ("MEL", "PER"),
        ("SYD", "ADL"),
    ]
    return {f"{a} → {b}": random.randint(200, 600) for a, b in routes}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/fetch', methods=['POST'])
def fetch():
    origin = request.form.get("origin")
    destination = request.form.get("destination")

    if not origin or not destination:
        return render_template("index.html", result={}, popular={})

    result = simulate_demand(origin.upper(), destination.upper())
    popular = get_popular_routes()
    return render_template("index.html", result=result, popular=popular)

@app.route('/api/data')
def api_data():
    data = simulate_demand("MEL", "SYD")
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)




