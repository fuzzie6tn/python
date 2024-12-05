# rain alert
import requests
from twilio.rest import Client


OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "3fc8982ac5d3a42b86c1b7b98927dd8a"
auth_id = "AC374d00f3d9b65735e032c4c4f99c6e81"
auth_token = "ca0f8b2735e7bf68a23ae2f172422d23"

weather_params = {
    "lat": 30.375320,
    "lon": 69.345116,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data(hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(auth_id, auth_token)
    message = client.messages \
         .create(
        body = "Bring an umbrella, it's going to rain today",
        from = "+18777804236",
        to = "=923435952375"
    )
    print(message.status)



