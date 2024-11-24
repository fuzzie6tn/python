# import requests
#
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("That resourse does not exist")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this resource")
# response.raise_for_status()
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

import requests
from datetime import datetime

MY_LAT = 30.375320
MY_LONG = 69.345116

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json" , params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split('T')[1].split(":")[0]
sunset = data["results"]["sunset"].split('T')[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)