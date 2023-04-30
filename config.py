import os

import dotenv

dotenv.load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
SCOPES = "playlist-modify-private playlist-modify-public user-top-read user-read-recently-played"
PLAYLIST_ID = os.getenv("PLAYLIST_ID")
