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
import smtplib
import time

MY_EMAIL = "fazilaroushanbeg@gmail.com"
PASSWORD = "apzvrhsadcimbzjl"

MY_LAT = 30.375320
MY_LONG = 69.345116

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = data["iss_position"]["longitude"]
    iss_latitude = data["iss_position"]["latitude"]

    if MY_LAT-5 <= iss_latitude <=  MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json" , params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True # it's dark

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.startls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Look Up!\n\nThe ISS is above you in the sky.")
