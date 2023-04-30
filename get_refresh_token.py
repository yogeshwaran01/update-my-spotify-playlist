import base64
import urllib.parse

import requests
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES

authorization_url = f"https://accounts.spotify.com/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={urllib.parse.quote_plus(SCOPES)}"

print()
print(authorization_url)
print()
print("Open url in the browser for authorization")
print()
print(
    "After authorization, Spotify will redirect you to another URL with authorization code. Copy the authorization code from URL and paste it below to get access token. Copy all tetters after `code=` in URL string"
)
print()

authorization_code = input("Authorization code: ")

auth_header = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_header_b64 = base64.b64encode(auth_header.encode("ascii")).decode("ascii")

headers = {"Authorization": f"Basic {auth_header_b64}"}

data = {
    "grant_type": "authorization_code",
    "code": authorization_code,
    "redirect_uri": REDIRECT_URI,
}

response = requests.post(
    "https://accounts.spotify.com/api/token", headers=headers, data=data
)
response_data = response.json()

print()
print(f"Refresh token: {response_data['refresh_token']}")
