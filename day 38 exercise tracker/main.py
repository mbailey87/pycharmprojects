import requests, os
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = os.environ.get('AppId')
API_KEY = os.environ.get('ApiKey')
HOST_DOMAIN = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = "/v2/natural/exercise"
SHEETY_USERNAME = os.environ.get('SheetyUsername')
USER = os.environ.get('user')
PASSWORD = os.environ.get('pass')


headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

exercise_params = {
    'query': input('What did you do for exercise and how long?\n'),
    'weight_kg': 77,
    'height_cm': 177.8,
    'age': 30
}

response = requests.post(url=f"{HOST_DOMAIN}{EXERCISE_ENDPOINT}", json=exercise_params, headers=headers)
data = response.json()['exercises'][0]
print(response.text)

print(data)

exercise = data['name'].title()
duration = data['duration_min']
calories = data['nf_calories']

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M")


sheety_url = f'https://api.sheety.co/{SHEETY_USERNAME}/myWorkouts/workouts'

workout ={
    "workout": {
    "date": date,
    "time": time,
    'exercise': exercise,
    "duration": duration,
    "calories": calories
}}

basic = HTTPBasicAuth(USER, PASSWORD)
workout_post = requests.post(url=sheety_url, json=workout, auth=basic)
print(workout_post.text)