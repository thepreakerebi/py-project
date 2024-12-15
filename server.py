from flask import Flask, render_template, request
from weather_call import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/weather", methods=["POST", "GET"])
def get_weather():
    if request.method == "POST":
        city = request.form.get("city")
        # city = request.args.get("city")

        if not bool(city.strip()):
            city = "Kigali"

        weather_data = get_current_weather(city)

        # city is not found by api
        if not weather_data['cod'] == 200:
            return render_template("city-not-found.html")
        
        return render_template(
            "weather.html", 
            title=weather_data["name"], 
            status=weather_data["weather"][0]["description"].capitalize(), 
            temp=f"{weather_data['main']['temp']:.1f}", 
            feels_like=f"{weather_data["main"]["feels_like"]:.1f}"
            )

    return render_template("index.html")

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)