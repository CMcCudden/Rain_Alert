import requests
from twilio.rest import Client
import os

ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
APP_ID = os.environ.get("APP_ID")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

MY_LAT = 42.868966
MY_LNG = -78.806113

parameters = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "appid": APP_ID,
        "exclude": "current,minutely,daily"
    }

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages \
        .create(
        body="IT'S GONNA RAIN, BRING AN UMBRELLA",
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
        )

    print(message.status)
