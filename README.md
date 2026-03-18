# Flask Weather App 🌤

A simple weather web app built with Flask and WeatherAPI.
Users can search any city to get real-time weather data.

---

## 🌐 Live Demo

https://flask-weather-v79n.onrender.com

---

## 🚀 Features

* Search weather by city
* Displays temperature, condition, and icon
* Input validation and error handling
* Clean centered UI

---

## 🛠 Tech Stack

* Python (Flask)
* HTML / CSS
* WeatherAPI
* Requests

---

## 📦 Setup

```bash
git clone https://github.com/visvinn/Flask-Weather.git
cd Flask-Weather
```

Create `.env`:

```text
WEATHER_API_KEY=your_api_key_here
```

Install & run:

```bash
pip install -r requirements.txt
python app.py
```

---

## ⚠️ Notes

* Uses free tier of WeatherAPI
* API key is stored via environment variables
* For local development, you can enable debug mode:

```python
app.run(debug=True)
```

---

## 👨‍💻 Author

Vinh Nguyen