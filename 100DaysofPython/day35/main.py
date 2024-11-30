# rain alert
import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "3fc8982ac5d3a42b86c1b7b98927dd8a"

weather_params = {
    "lat": 30.375320,
    "lon": 69.345116,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)



