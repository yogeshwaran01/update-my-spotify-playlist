from abc import ABC
from dataclasses import dataclass

import spotipy


@dataclass
class TimeRange:
    """Time Range class for ease configuration"""

    long_term = "long_term"
    medium_term = "medium_term"
    short_term = "short_term"


class TopCategoriesBase(ABC):
    """Absract base class for Top Contents"""

    def __init__(
        self, time_range=TimeRange.medium_term, no_of_tracks_required=10
    ) -> None:
        self.time_range = time_range
        self.no_of_tracks_required = no_of_tracks_required


class TopArtist(TopCategoriesBase):
    def _get_tracks(self, sp: spotipy.Spotify) -> list:
        """Returns URI of tracks based on current user top artists"""
        top_artists = sp.current_user_top_artists(limit=5, time_range=self.time_range)
        artists_ids = [artist["id"] for artist in top_artists["items"]]
        recommenations = sp.recommendations(
            seed_artists=artists_ids, limit=self.no_of_tracks_required
        )["tracks"]
        return [t["uri"] for t in recommenations]


class TopTracks(TopCategoriesBase):
    def _get_tracks(self, sp: spotipy.Spotify) -> list:
        """Returns URI of tracks based on current user top tracks"""
        top_tracks = sp.current_user_top_tracks(limit=5, time_range=self.time_range)
        tracks_ids = [track["id"] for track in top_tracks["items"]]
        recommenations = sp.recommendations(
            seed_tracks=tracks_ids, limit=self.no_of_tracks_required
        )["tracks"]
        return [t["uri"] for t in recommenations]


class TopMix(TopCategoriesBase):
    def _get_tracks(self, sp: spotipy.Spotify) -> list:
        """Returns URI of tracks based on current user top artists and top tracks"""
        top_tracks = sp.current_user_top_tracks(limit=3, time_range=self.time_range)
        tracks_ids = [track["id"] for track in top_tracks["items"]]
        top_artists = sp.current_user_top_artists(limit=2, time_range=self.time_range)
        artists_ids = [artist["id"] for artist in top_artists["items"]]
        recommenations = sp.recommendations(
            seed_tracks=tracks_ids,
            limit=self.no_of_tracks_required,
            seed_artists=artists_ids,
        )["tracks"]
        return [t["uri"] for t in recommenations]


class RecentlyPlayed:
    def __init__(self, no_of_tracks_required=10) -> None:
        self.no_of_tracks_required = no_of_tracks_required

    def _get_tracks(self, sp: spotipy.Spotify) -> list:
        """Returns URI of tracks based on current user top artists"""
        recently_played = sp.current_user_recently_played(limit=5)
        tracks_ids = []
        for item in recently_played["items"]:
            if item["track"]:
                tracks_ids.append(item["track"]["id"])
        recommenations = sp.recommendations(
            seed_tracks=tracks_ids, limit=self.no_of_tracks_required
        )["tracks"]
        return [t["uri"] for t in recommenations]


# class TopGenres(TopCategoriesBase):
#     def _get_tracks(self, sp: spotipy.Spotify):
#         top_artists = sp.current_user_top_artists(
#             limit=5, time_range=self.time_range
#         )
#         genres = []
#         _genres = [artist["genres"] for artist in top_artists["items"]]
#         for g in _genres:
#             for i in g:
#                 genres.append(i)
#         recommenations = sp.recommendations(
#             seed_genres=genres[:4], limit=self.no_of_tracks_required
#         )["tracks"]
#         return [t["uri"] for t in recommenations]


class Artist:
    def __init__(self, id) -> None:
        self.id = id


class Track:
    def __init__(self, id) -> None:
        self.id = id


class Genre:
    def __init__(self, genre) -> None:
        self.genre = genre


class Mix:
    def __init__(self, mix, no_of_tracks_required=30) -> None:
        if len(mix) > 5:
            raise Exception("Only contains 5 conditions")
        else:
            self.mix = mix
            self.no_of_tracks_required = no_of_tracks_required

    def _get_tracks(self, sp) -> list:
        """Returns URI of tracks based on current user top artists"""
        tracks = []
        artist = []
        genres = []
        for m in self.mix:
            if type(m) == Track:
                tracks.append(m.id)
            elif type(m) == Artist:
                artist.append(m.id)
            elif type(m) == Genre:
                genres.append(m.genre)
            else:
                pass
        recommenations = sp.recommendations(
            limit=self.no_of_tracks_required,
            seed_artists=artist,
            seed_tracks=tracks,
            seed_genres=genres,
        )["tracks"]
        return [t["uri"] for t in recommenations]
