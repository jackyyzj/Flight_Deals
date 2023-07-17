import requests
from flight_data import FlightData
import os

TEQUILA_ENDPOINT = os.environ.get("TEQUILA_ENDPOINT")
API_KEY = os.environ.get("API_KEY")

class FlightSearch:
    def get_destination_code(self, city_name):

        params = {
            "term": city_name,
            "location_types": "city"
        }
        header = {
            "apikey": API_KEY
        }

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        data = requests.get(location_endpoint, params = params, headers = header)
        json_data = data.json()["locations"]
        code = json_data[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        headers = {
            "apikey": API_KEY
        }

        response = requests.get(url = f"{TEQUILA_ENDPOINT}/v2/search", params = params, headers= headers)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        else:
            flight_data = FlightData(data["price"],
                data["route"][0]["cityFrom"],
                data["route"][0]["flyFrom"],
                data["route"][0]["cityTo"],
                data["route"][0]["flyTo"],
                data["route"][0]["local_departure"].split("T")[0],
                data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
            return flight_data
