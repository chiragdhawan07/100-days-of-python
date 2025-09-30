class FlightData:
    """
    A simple class to hold details about a single flight.
    """

    def __init__(self, price, origin_airport, destination_airport, out_date, return_date):
        # Flight ticket cost
        self.price = price
        # IATA code of departure airport
        self.origin_airport = origin_airport
        # IATA code of arrival airport
        self.destination_airport = destination_airport
        # Departure date
        self.out_date = out_date
        # Return date
        self.return_date = return_date


def find_cheapest_flight(data):
    """
    Go through the Amadeus API flight data and find the cheapest option.

    Args:
        data (dict): The flight data returned by Amadeus API.

    Returns:
        FlightData: object holding the cheapest flight details.
                    If nothing found, returns FlightData with "N/A".
    """

    # If no flights or API failed → return N/A flight
    if data is None or not data.get("data"):
        print("⚠️ No flight data available.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Assume the first flight is cheapest
    first = data["data"][0]
    lowest_price = float(first["price"]["grandTotal"])
    origin = first["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    # Loop over all flights and check if any are cheaper
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"✅ New lowest price: £{lowest_price} to {destination}")

    return cheapest_flight
