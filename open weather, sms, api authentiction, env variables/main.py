import requests
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()  # This loads the environment variables from .env

import os

# Now, you can get your API key like this:
api_key = os.environ.get("OWM_API_KEY") 
print("API Key:", os.environ.get("OWM_API_KEY"))


api_key=os.environ.get("OWM_API_KEY")
print(api_key)
account_sid="Account sid"
auth_token="auth token"
parameters={
    "lat": 36.25,
    "lon": 44.48,
    "cnt": 4,
    "appid": api_key
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameters)
response.raise_for_status()
weather_data=response.json()

will_rain=False
for i in weather_data["list"]:
    condition_code=i["weather"][0]["id"]
    if condition_code<700:
        will_rain=True

if will_rain:
    # print("bring an umbrella")
    client = Client(account_sid, auth_token)
    message=client.messages \
    .create(
        body="It's going to rain today, take an ☔️",
        from_="+18886585140",
        to="+1 571 528 2985"
    )
    print(message.status)
