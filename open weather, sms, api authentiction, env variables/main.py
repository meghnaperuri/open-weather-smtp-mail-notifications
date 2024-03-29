import requests
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()  # This loads the environment variables from .env

import os

# Now, you can get your API key like this:
api_key = os.environ.get("OWM_API_KEY") 
print("API Key:", os.environ.get("OWM_API_KEY"))


# https://api.openweathermap.org/data/2.5/weather?lat=38.854004&lon=-77.356918&appid=27f71744ae8759f44a23ca4666152852
# recovery code for twilio: QGF1UXTJCYAAXMT1HEBXCT3X
# auth token: 14bd25b6f9b9a602ee88ade1e5200b8a
# Account SID: AC745b3efe5a29e2ba5d33516e237fe777
# twillio phone number: +18777804236
# "lat": 38.854004,
# "lon": -77.356918,
api_key=os.environ.get("OWM_API_KEY")
print(api_key)
account_sid="AC745b3efe5a29e2ba5d33516e237fe777"
auth_token="14bd25b6f9b9a602ee88ade1e5200b8a"
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