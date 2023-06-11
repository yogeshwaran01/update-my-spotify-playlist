import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config import PLAYLISTS
from envs import *

sp = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPES,
)

token = sp.refresh_access_token(REFRESH_TOKEN)
access_token = token["access_token"]

spotify = spotipy.Spotify(auth=access_token)

for playlist in PLAYLISTS:

    uris = playlist['category']._get_tracks(spotify)

    spotify.playlist_replace_items(playlist['id'], uris)
    print("Done")
