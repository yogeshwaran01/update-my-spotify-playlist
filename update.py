import spotipy
from spotipy.oauth2 import SpotifyOAuth

from config import *

sp = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPES,
)

token = sp.refresh_access_token(REFRESH_TOKEN)
access_token = token["access_token"]

spotify = spotipy.Spotify(auth=access_token)

top_artists = spotify.current_user_top_artists(limit=5, time_range="medium_term")
top_tracks = spotify.current_user_top_tracks(limit=2, time_range="medium_term")
recently_played = spotify.current_user_recently_played(limit=3)

artists = [artist["id"] for artist in top_artists["items"]]
tracks = [track["id"] for track in top_tracks["items"]]

for item in recently_played["items"]:
    if item["track"]:
        tracks.append(item["track"]["id"])


recommendations_based_on_tracks = spotify.recommendations(seed_tracks=tracks)
recommendations_based_on_artists = spotify.recommendations(seed_artists=artists)

recommendations = recommendations_based_on_tracks["tracks"]
recommendations.extend(recommendations_based_on_artists["tracks"])

uris = []

for t in recommendations:
    uris.append(t["uri"])

spotify.playlist_replace_items(PLAYLIST_ID, uris)

print("Done")
