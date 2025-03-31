import os
import requests
from dotenv import load_dotenv

load_dotenv()


IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):

        self._api_key = os.getenv('APIKEY')
        self._api_secret = os.getenv('APISECRET')
        self.url = 'https://test.api.amadeus.com/v1'
        self.params = {
            "grant_type": 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret

        }
        print(self._api_key)
        print(self._api_secret)
        print(self.params)

        self._token = self.get_new_token()


    def get_iata_code(self, city_name):
        response = requests.get(url=IATA_ENDPOINT,
                                headers = {
                                "Authorization": f"Bearer {self._token}"
                                },
                                params={'keyword':city_name.upper()})
        data = response.json()['data'][0]['iataCode']
        return data

    def get_new_token(self):

        header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=self.params)
        print(response.status_code)
        print(response.json()['access_token'])
        return response.json()['access_token']

    def check_flights(self, origin_code, destination_code, from_date, to_date):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_code,
            "destinationLocationCode": destination_code,
            "departureDate": from_date.strftime("%Y-%m-%d"),
            "returnDate": to_date.strftime("%Y-%m-%d"),
            'adults': 1,
            'nonStop': 'true',
            "currencyCode": "GBP",
            'max': "10"
        }
        response = requests.get(url=FLIGHT_ENDPOINT, headers=headers, params=query)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        data = response.json()['data']
        print(data)
        return data