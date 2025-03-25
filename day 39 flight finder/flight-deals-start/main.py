
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager


data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = flight_search.get_iata_code(row['city'])

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()


