# Exercise Tracking with Python and Google Sheets

import requests
import json  # Import the json module for loading the JSON file
from datetime import datetime

# Personal details for the API
GENDER = "female"
WEIGHT_KG = 52
HEIGHT_CM = 162
AGE = 21

# Load the sensitive data from the JSON file
try:
    with open("data.json", "r") as json_file:
        config = json.load(json_file)
        APP_ID = config["ENV_NIX_APP_ID"]
        API_KEY = config["ENV_NIX_API_KEY"]
        sheet_endpoint = config["SHEETY_ENDPOINT"]
        sheet_username = config["SHEETY_USERNAME"]
        sheet_password = config["SHEETY_PASSWORD"]
        sheet_token = config["SHEETY_TOKEN"]
except FileNotFoundError:
    raise FileNotFoundError(
        "The data.json file was not found. Please ensure it is in the same directory as this script.")
except KeyError as e:
    raise KeyError(f"Missing key {e} in the data.json file. Please ensure all required keys are present.")

# Nutrition API Endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Taking user input
exercise_text = input("Tell me which exercises you did: ")

# Adding headers and parameters to send API requests
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Making the Nutrition API request
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutrition API call: \n {result} \n")

# Formatting the date and time for output
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Iterate through exercises and send data to Google Sheets
GOOGLE_SHEET_NAME = "My_workouts"

for exercise in result.get("exercises", []):  # Ensures no KeyError if "exercises" is missing
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # Sending data to Sheety using authentication
    if sheet_token:
        # Use Bearer token header authentication if provided
        bearer_headers = {
            "Authorization": f"Bearer {sheet_token}"
        }
        sheet_response = requests.post(
            sheet_endpoint,
            json=sheet_inputs,
            headers=bearer_headers
        )
    else:
        # Fallback to basic authentication
        sheet_response = requests.post(
            sheet_endpoint,
            json=sheet_inputs,
            auth=(sheet_username, sheet_password)
        )

    print(f"Sheety Response: \n {sheet_response.text}")
