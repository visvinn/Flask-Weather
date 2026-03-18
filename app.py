from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1"
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Please enter a city."
        else:
            params = {
                "key": API_KEY,
                "q": city
            }
            response = requests.get(f"{BASE_URL}/current.json", params=params)
            data = response.json()
            if "error" in data:
                error = data["error"]["message"]
            else:
                weather = data
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run()