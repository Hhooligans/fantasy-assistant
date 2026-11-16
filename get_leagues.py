import os
import requests

response = requests.post(
    "https://api.login.yahoo.com/oauth2/get_token",
    auth=(
        os.environ["YAHOO_CLIENT_ID"],
        os.environ["YAHOO_CLIENT_SECRET"]
    ),
    data={
        "grant_type": "refresh_token",
        "refresh_token": os.environ["YAHOO_REFRESH_TOKEN"]
    }
)

response.raise_for_status()

access_token = response.json()["access_token"]

headers = {
    "Authorization": f"Bearer {access_token}"
}

r = requests.get(
    "https://fantasysports.yahooapis.com/fantasy/v2/game/nfl",
    headers=headers,
)

print("STATUS:", r.status_code)
print(r.text)
