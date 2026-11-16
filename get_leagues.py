import os
import requests
import json

CLIENT_ID = os.environ["YAHOO_CLIENT_ID"]
CLIENT_SECRET = os.environ["YAHOO_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["YAHOO_REFRESH_TOKEN"]

response = requests.post(
    "https://api.login.yahoo.com/oauth2/get_token",
    auth=(CLIENT_ID, CLIENT_SECRET),
    data={
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    },
)

response.raise_for_status()

token_data = response.json()

print("TOKEN RESPONSE:")
print(json.dumps(token_data, indent=2))
