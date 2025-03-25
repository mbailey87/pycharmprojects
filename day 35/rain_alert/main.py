import requests
import os
from twilio.rest import Client
API_KEY = os.environ.get('OWM_API_KEY')
parameters= {
    "q": "Lehi,UT,US",
    "appid": API_KEY,
    'cnt':4
}


response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
data = response.json()['list']

weather = [(period['weather'][0]['id'], period['dt_txt'])  for period in data]

account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')
client = Client(account_sid, auth_token)

twilio_number = '+18889779221'



print(weather)
is_raining = False
bring_umbrella = [is_raining == True for (code, time) in weather if code < 700]
if is_raining:
    message = client.messages.create(
        body="Bring an umbrella",
        from_=twilio_number,
        to="+18016693215"
    )
    print(message.status)
else:
    message = client.messages.create(
        body="No need to bring an umbrella today",
        from_=twilio_number,
        to="+18016693215"
    )
    print(message.status)

