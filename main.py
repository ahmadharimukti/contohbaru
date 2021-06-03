from flask import Flask,request
import os, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data={"lat": 33.44, "lon": -94.04,  "timezone": "America/Chicago",  "timezone_offset": -21600,  "current": {    "dt": 1618317040,    "sunrise": 1618282134,    "sunset": 1618333901, "temp": 284.07,"feels_like": 282.84,"pressure": 1019, "humidity": 62,"dew_point": 277.08,"uvi": 0.89,"clouds": 0,"visibility": 10000,"wind_speed": 6,"wind_deg": 300}}
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",2000)))
