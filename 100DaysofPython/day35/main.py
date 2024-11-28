# rain alert
import requests

OWM_endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "7dfde1fd0c46b729c827bd2db6c326f0"

weather_params = {
    "lat": 30.375320,
    "lon": 69.345116,
    "appid": api_key,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
hourly_data = response.json()
print(hourly_data['hourly'])




