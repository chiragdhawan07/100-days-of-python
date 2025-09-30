import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load API credentials from .env
load_dotenv()

# Amadeus API endpoints (test environment)
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"


class FlightSearch:
    """
    Class to interact with Amadeus API:
    - Get airport IATA codes
    - Search for flights
    """

    def __init__(self):
        # Grab API key & secret from .env
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_SECRET")

        # Request a fresh token (usually lasts ~30 min)
        self._token = self._get_new_token()

    def _get_new_token(self):
        """
        Get a new authentication token from Amadeus API.
        """
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        data = response.json()

        print(f"🔑 Token: {data.get('access_token')}")
        print(f"⏳ Expires in: {data.get('expires_in')} sec")

        return data.get("access_token")

    def get_destination_code(self, city_name):
        """
        Get the IATA code for a given city name.
        Example: 'London' -> 'LON'
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}

        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        print(f"🌍 Looking up IATA for {city_name} → Status {response.status_code}")

        try:
            code = response.json()["data"][0]["iataCode"]
            return code
        except IndexError:
            print(f"⚠️ No airport code found for {city_name} (IndexError).")
            return "N/A"
        except KeyError:
            print(f"⚠️ Unexpected response structure for {city_name} (KeyError).")
            return "Not Found"

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Search for flights between two cities within given dates.
        """
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            print(f"❌ Flight search failed. Code: {response.status_code}")
            print("Response:", response.text)
            return None

        print(f"✈️ Found flights from {origin_city_code} → {destination_city_code}")
        return response.json()
