import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# -------- Personal Details -------- #
GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 180
AGE = 21

# -------- API Credentials -------- #
APP_ID = os.getenv("ENV_NIX_APP_ID")
API_KEY = os.getenv("ENV_NIX_API_KEY")
SHEET_ENDPOINT = os.getenv("ENV_SHEETY_ENDPOINT")
SHEETY_USERNAME = os.getenv("ENV_SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("ENV_SHEETY_PASSWORD")
SHEETY_TOKEN = os.getenv("ENV_SHEETY_TOKEN")

# Nutritionix API endpoint
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# -------- Ask user for workout -------- #
exercise_text = input("💪 What exercises did you do today? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# -------- Nutritionix Request -------- #
response = requests.post(EXERCISE_ENDPOINT, json=params, headers=headers)
data = response.json()

# -------- Date & Time -------- #
today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%H:%M:%S")

# -------- Send Data to Google Sheet -------- #
for exercise in data["exercises"]:
    workout_entry = {
        "workout": {
            "date": today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # --- Option 1: Basic Auth ---
    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=workout_entry,
        auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
    )

    # --- Option 2: Bearer Token Auth ---
    # headers = {"Authorization": f"Bearer {SHEETY_TOKEN}"}
    # sheet_response = requests.post(SHEET_ENDPOINT, json=workout_entry, headers=headers)

    print(sheet_response.text)
