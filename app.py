# Example using Flask (adjust for other frameworks)
from flask import Flask, jsonify, request
from procyclingstats import Rider  # Assuming you have installed the library

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to the PCS API"

@app.route("/rider/<name>")
def get_rider_info(name):
    try:
        rider = Rider(f"rider/{name}")
        rider_data = rider.parse()
        return jsonify(rider_data), 200  # Return data and status code
    except Exception as e:
        print(f"Error fetching rider data: {e}")
        return jsonify({"error": "An error occurred"}), 500  # Handle errors

if __name__ == "__main__":
    app.run(debug=False)  # Set debug=False in production
