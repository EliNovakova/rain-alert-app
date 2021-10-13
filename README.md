# Rain Alert App
Checks the weather forecast for the next 12 hours (based on user's location)
and in case of rain, sends a text message to notify a user to bring an umbrella.

## How to use

This app requires OpenWeatherMap and Twilio account for the API to work.

These parameters need to be set:
```python
API_KEY = "<INSERT-API-KEY>" # OpenWeatherMap
ACCOUNT_SID = "<INSERT-ACCOUNT_SID>" # Twilio
AUTH_TOKEN = "<INSERT-AUTH_TOKEN>" # Twilio
MY_LAT = <INSERT-LAT>
MY_LONG = <INSERT-LONG>
MY_PHONE_NUM = "<INSERT-YOUR-PHONE-NUM>"
TWILIO_PHONE_NUM = "<INSERT-TWILIO-PHONE-NUM>" # Twilio
```