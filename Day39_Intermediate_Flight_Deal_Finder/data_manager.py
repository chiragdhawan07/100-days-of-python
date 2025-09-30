import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# load all values from .env file
load_dotenv()

# Sheety endpoint for your Google Sheet
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")


class DataManager:
    """
    This class talks to the Google Sheet via Sheety API.
    It can get all the rows and also update the IATA codes.
    """

    def __init__(self):
        # if you turned on auth in Sheety, read username & password from env
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")

        # only use auth if both values exist
        if self.username and self.password:
            self.auth = HTTPBasicAuth(self.username, self.password)
        else:
            self.auth = None

        self.destination_data = {}

    def get_destination_data(self):
        """Fetches the sheet data and stores it inside self.destination_data"""
        if self.auth:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT, auth=self.auth)
        else:
            response = requests.get(url=SHEETY_PRICES_ENDPOINT)

        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        print("Sheet data downloaded ✅")
        return self.destination_data

    def update_destination_codes(self):
        """Updates the IATA code for each city in the sheet"""
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            if self.auth:
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data,
                    auth=self.auth
                )
            else:
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data
                )

            response.raise_for_status()
            print(f"Updated {city['city']} → {city['iataCode']}")
