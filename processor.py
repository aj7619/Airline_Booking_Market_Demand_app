import random

def simulate_demand(origin, destination):
    # Simulated 6-month demand trend
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    values = [random.randint(100, 500) for _ in months]

    return {
        "labels": months,
        "values": values
    }
def top_routes():
    # Simulated top 5 routes with random demand values
    routes = {
        "DEL → BOM": random.randint(300, 600),
        "BOM → BLR": random.randint(300, 600),
        "MEL → SYD": random.randint(300, 600),
        "NYC → LAX": random.randint(300, 600),
        "SYD → PER": random.randint(300, 600),
    }
    return routes
