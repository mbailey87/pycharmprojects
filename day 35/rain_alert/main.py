import requests
API_KEY = "71e28b960b847a0b52b2ed947ab700fd"
parameters= {
    "q": "Lehi,UT,US",
    "appid": API_KEY,
    'cnt':4
}


response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()['list']

weather = [(period['weather'][0]['id'], period['dt_txt'])  for period in data]

print(weather)

