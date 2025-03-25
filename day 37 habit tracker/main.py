import requests
import datetime as dt

USERNAME = "mattbailey87"
PASSWORD = "asdfasdafefasdf"
pixela_endpoint = 'https://pixe.la/v1/users'


users_params = {
    "token": PASSWORD,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    "notMinor": 'yes'
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)

graph_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": 'graph1',
    'name': 'coding graph',
    'unit': "hour",
    'type': "float",
    'color': 'sora'
}
headers = {
    "X-USER-TOKEN": PASSWORD
}
# response = requests.post(url=graph_enpoint, json=graph_config, headers=headers)
# print(response.text)

now = dt.datetime.now()
today = now.strftime("%Y%m%d")
print(today)
pixel_config = {
    'date': today,
    'quantity': "4.5",

}

pixel_creation = f"{graph_enpoint}/{graph_config['id']}"

# response = requests.post(url=pixel_creation, json=pixel_config, headers=headers)
# print(response.text)

update_params = {
    "quantity": "6.0"
}

# response = requests.put(url=f"{pixel_creation}/20250324", json={"quantity": "6.0"}, headers=headers)
# print(response.text)


response = requests.delete(url=f"{pixel_creation}/20250324", headers=headers)
print(response.text)