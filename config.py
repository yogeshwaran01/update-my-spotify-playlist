import os

import dotenv

from categories import *

dotenv.load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
SCOPES = "playlist-modify-private playlist-modify-public user-top-read user-read-recently-played"
PLAYLIST_ID = os.getenv("PLAYLIST_ID")

# Insert your category here

CATEGORY = TopMix(time_range=TimeRange.long_term, no_of_tracks_required=30)

# Available categories
# ---------------------
# 1) TopArtist(time_range=TimeRange.long_term, no_of_tracks_required=34)
# 2) TopTracks(time_range=TimeRange.short_term, no_of_tracks_required=22)
# 3) TopMix()
# 4) RecentlyPlayed()

# 5) Mix(
#     [
#         Artist("7jVv8c5Fj3E9VhNjxT4snq"),
#         Artist("6M2wZ9GZgrQXHCFfjv46we"),
#         Artist("1Xyo4u8uXC1ZmMpatF05PJ"),
#         Genre("pop"),
#         Track("0HqZX76SFLDz2aW8aiqi7G"),
#     ]
# )

# In Mix you can mix upto 5 parameter like Artist, Genre and Track. Only 5 parameter are allowed
# Example
# CATEGORY = Mix(
#     [
#         Artist("7jVv8c5Fj3E9VhNjxT4snq"),
#         Artist("6M2wZ9GZgrQXHCFfjv46we"),
#         Artist("1Xyo4u8uXC1ZmMpatF05PJ"),
#         Genre("pop"),
#         Track("0HqZX76SFLDz2aW8aiqi7G"),
#     ]
# )
