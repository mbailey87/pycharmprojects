import requests, datetime as dt, smtplib, time
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
iss_longitude = float(iss_data['iss_position']['longitude'])
iss_latitude = float(iss_data['iss_position']['latitude'])

test_gmail = "matthewstestingemail87@gmail.com"
password = "ddfi tksv drsp dnhu"

iss_position = (iss_longitude, iss_latitude)
print(iss_position)
print(int(iss_longitude), int(iss_latitude))

lat = -16
long = 92

local_location = (long,lat)

parameters = {
    "lat": lat,
    'lng': long,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(":")[0]
sunset = data['results']['sunset'].split('T')[1].split(":")[0]
print(data)

print(sunrise, sunset )

sunrise_hour = int(sunrise)
sunset_hour = int(sunset)

if sunset_hour < 6:
    sunset_hour = 24 - 6 + sunset_hour
else:
    sunset_hour -= 6

if sunrise_hour < 6:
    sunrise_hour = 24 - sunrise_hour
else:
    sunrise_hour -= 6

print(sunset_hour, sunrise_hour)

now = dt.datetime.now()
hour = 20


def check_iss():
    if sunrise_hour <= hour <= sunset_hour:
        print("day time")
    else:
        if lat -6 < iss_latitude < lat + 6 and long - 6 < iss_longitude < long + 6:
            with smtplib.SMTP('smtp.gmail.com') as connection:
                connection.starttls()
                connection.login(user=test_gmail, password=password)
                connection.sendmail(from_addr=test_gmail, to_addrs='matthewtestingemail@yahoo.com', msg="Subject:Iss Position\n\nlook up")

            print('look up')
        else:
            print("its not over head")

while True:
    check_iss()
    time.sleep(60)

