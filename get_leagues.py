import os
import requests
import json

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

data = response.json()

safe = {}

for k, v in data.items():
    if "token" not in k.lower():
        safe[k] = v

print(json.dumps(safe, indent=2))
