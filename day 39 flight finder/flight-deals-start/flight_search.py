import os
import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("APIKEY")
        self._api_secret = os.environ.get("APISECRET")
        self.url = 'https://test.api.amadeus.com/v1'
        self.params = {
            "grant_type": 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret

        }
        self._token = self.get_new_token()


    def get_iata_code(self, city_name):
        response = requests.get(url=f'{self.url}/reference-data/locations/cities',
                                headers = {
                                "Authorization": f"Bearer {self._token}"
                                },
                                params={'keyword':city_name.upper()})
        data = response.json()['data'][0]['iataCode']
        return data

    def get_new_token(self):

        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=f"{self.url}/security/oauth2/token", headers=header, data=self.params)
        response.raise_for_status()
        return response.json()['access_token']