import os
import requests

CLIENT_ID = os.environ["YAHOO_CLIENT_ID"]
CLIENT_SECRET = os.environ["YAHOO_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["YAHOO_REFRESH_TOKEN"]

# Get access token
response = requests.post(
    "https://api.login.yahoo.com/oauth2/get_token",
    auth=(CLIENT_ID, CLIENT_SECRET),
    data={
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
    },
)

response.raise_for_status()

access_token = response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}",
    "Accept": "application/json",
}

# Get current user info first
r = requests.get(
    "https://fantasysports.yahooapis.com/fantasy/v2/users;use_login=1",
    headers=headers,
)

print("STATUS:", r.status_code)
print("CONTENT-TYPE:", r.headers.get("content-type"))
print(r.text)
