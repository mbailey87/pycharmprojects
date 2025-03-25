from flight_search import FlightSearch
import datetime as dt
import requests


class FlightData():
    def __init__(self, price="N/A",origin_airport="N/A",destination_airport="N/A",out_date="N/A", return_date="N/A"):

        self.originLocationCode = origin_airport

        self.destination_airport = destination_airport

