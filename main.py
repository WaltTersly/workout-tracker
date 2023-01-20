import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 167
AGE = 25

APP_ID = "79229ccb"
APP_KEY = "ed55db9c55cb0bdcccf5d16586295cb1"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = os.environ["ENV_SHEET_ENDPOINT"]

sheet_header = {
    "Authorization": "Basic dGVyc2x5cGFyYWRpc2U6bG9zdGxvc3Qx"
}

sheet_username = os.environ["ENV_SHEETY_USERNAME"]
sheet_password = os.environ["ENV_SHEETY_PASSWORD"]

exercise_text = input("Tell me which exercises you did: ").lower()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

body_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=body_params, headers=headers)
result = response.json()
response.raise_for_status()
print(result)

exercises = [
    {
        "name":  data["name"],
        "duration": data['duration_min'],
        "calories": data['nf_calories']
    } for data in response.json()['exercises']
]


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 2: Basic Auth
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            sheet_username,
            sheet_password,
        )
    )

    print(sheet_response.text)
