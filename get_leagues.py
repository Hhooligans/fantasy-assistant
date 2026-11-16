import json
import os
import requests

CLIENT_ID = os.environ["YAHOO_CLIENT_ID"]
CLIENT_SECRET = os.environ["YAHOO_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["YAHOO_REFRESH_TOKEN"]

# Exchange refresh token for access token
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
access_token = token_data["access_token"]

# Get Yahoo Fantasy game list
headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json",
}

r = requests.get(
    "https://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1/games",
    headers=headers,
)

print(r.text)
