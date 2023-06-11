from categories import *

# Add Your Playlist id and its category

PLAYLISTS = [
    {
        'id': '2fABBrRXVPr2d6UT4S3f2L',
        'category': RecentlyPlayed(no_of_tracks_required=30)
    },
    {
        'id': '7rJuai1MjSx0h99zZIK0Je',
        'category': Mix(
            [
                Artist('1mYsTxnqsietFxj1OgoGbG'),
                Artist('6IHhDsmQhMdqnKIb2sE41H'),
                Artist('6AiX12wXdXFoGJ2vk8zBjy'),
                Artist('4zCH9qm4R2DADamUHMCa6O'),
                Artist('6CtYzQvENTdGq5LPPsePdV')
            ],
            no_of_tracks_required=50
        )
    },
    {
        'id': '6n559itEfTJWdWpQiPZSxE',
        'category': Mix(
            [
                Artist('6M2wZ9GZgrQXHCFfjv46we'),
                Artist('5Pwc4xIPtQLFEnJriah9YJ'),
                Artist('1Xyo4u8uXC1ZmMpatF05PJ'),
                Artist('53XhwfbYqKCa1cC15pYq2q'),
                Genre('pop')
            ],
            no_of_tracks_required=50
        )
    },
    {
        'id': '5X8TGKcqbaOyeFf2vxg3YJ',
        'category': TopMix(no_of_tracks_required=30)
    },
    {
        'id': '1xOBtxXq8zR5azITxc7xDj',
        'category': Mix(
            [
                Artist('1mYsTxnqsietFxj1OgoGbG'),
                Artist('6IHhDsmQhMdqnKIb2sE41H'),
                Artist('6AiX12wXdXFoGJ2vk8zBjy'),
                Artist('6M2wZ9GZgrQXHCFfjv46we'),
                Artist('5Pwc4xIPtQLFEnJriah9YJ'),
            ], no_of_tracks_required=30
        )
    }

    
]


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


### Example Config File:

# PLAYLISTS = [
#     {
#         'id': '2bx19B2bwgTf20XWQBxlQo',
#         'category': TopMix(time_range=TimeRange.long_term, no_of_tracks_required=30)
#     },
#     {
#         'id': '2bx19B2bwgTff20XWQBxlQo',
#         'category': TopArtist(time_range=TimeRange.short_term, no_of_tracks_required=30)
#     },
#     {
#         'id': '7sLWB2thlLWFcvuExsc77y',
#         'category': Mix(
#             [
#                 Artist('7dGJo4pcD2V6oG8kP0tJRR'),
#                 Artist('1mYsTxnqsietFxj1OgoGbG'),
#                 Genre('pop')
#             ],
#             no_of_tracks_required=20
#         )
#     },
#     {
#         'id': '23ljfjfwfpwjwjfwjfjfjs',
#         'category': RecentlyPlayed(no_of_tracks_required=23)
#     }
# ]
