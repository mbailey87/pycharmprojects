import requests
from pprint import pprint
import os
from requests.auth import HTTPBasicAuth

SHEETY_URL = 'https://api.sheety.co/1947475f6fc6d6356a65c37b04a1895b/flightDeals/prices'


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.token = os.environ.get("SHEETYBEARERTOKEN")
        self.user = os.environ.get('SHEETYUSERNAME')
        self.basic = HTTPBasicAuth(username=self.user, password=self.token)
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_URL, auth=self.basic)
        response.raise_for_status()
        self.destination_data = response.json()['prices']

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            update_iata = requests.put(url=f'{SHEETY_URL}/{city['id']}', json=new_data, auth=self.basic)
            update_iata.raise_for_status()
            print(update_iata.text)
