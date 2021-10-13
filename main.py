import requests
from twilio.rest import Client


API_KEY = "<INSERT-API-KEY>"    # OpenWeatherMap
ACCOUNT_SID = "<INSERT-ACCOUNT_SID>"    # Twilio
AUTH_TOKEN = "<INSERT-AUTH_TOKEN>"      # Twilio

MY_LAT = <INSERT-LAT>    # Your latitude as float
MY_LONG = <INSERT-LONG>   # Your longitude as float

MY_PHONE_NUM = "<INSERT-YOUR-PHONE-NUM>"        # Has to be verified in Twilio
TWILIO_PHONE_NUM = "<INSERT-TWILIO-PHONE-NUM>"  # Can be generated after signing up to Twilio

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()


twelve_hour_list = []
for hour in range(12):      # get id of the weather condition of the next 12 hours
    hourly_data = weather_data["hourly"][hour]["weather"][0]["id"]
    twelve_hour_list.append(hourly_data)

for i in twelve_hour_list:
    if i < 700:     # if there is a weather condition id lower than 700 (means rain), notify user that it's going to rain
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages \
            .create(
            body="It's going to rain today. Remember to bring an umbrella ☂.",
            from_=TWILIO_PHONE_NUM,
            to=MY_PHONE_NUM
        )
        print(message.status)
        break

