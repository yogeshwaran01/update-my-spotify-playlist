# update-my-Spotify-playlist

Automatically update your Spotify playlist with tracks of your favorite artists and genres using this Python script powered by the Spotify Web API and GitHub Actions.

## Introduction

Update My Spotify Playlist is a Python tool that streamlines your Spotify playlist management by adding your favourite tracks from your favorite artists to your playlist in real-time.

## Usage

1. Fork this repo
2. Clone your repo in local
3. copy `.env-template` into `.env`
4. Install all Python requirements in `requirements.txt`
5. Go to the Spotify Developer Dashboard and log in with your Spotify account.
6. Click on the "Create an App" button and fill out the necessary information, such as the name and description of your application. Use `http://localhost:5000` as redirect URL
7. Once you've created the app, you'll be taken to the app dashboard. Here, you'll find your client ID, client secret and Redirect URL. Copy this and paste it your `.env` file
8. Create new playlist in your Spotify Account and copy the playlist id from the url. Paste the playlist id in `.env` file.
9. Run this Script `get_refresh_token.py` to get refresh token. Follow the instruction in this script. Copy the refresh token into `.env` file.
10. Run this Script `update.py` for testing.
11. Add all env variable `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI`, `REFRESH_TOKEN`, `PLAYLIST_ID` in github repository secret. Checkout this [link](https://docs.github.com/en/actions/reference/encrypted-secrets) to add a new repository secret.
12. By default it updates daily at `2:47 UTC`. You can also change this by changing the cron in `/.github/workflows/main.yml` by using [Cron Generator](https://crontab.guru/).

## Playlist customization

Your playlist can be customized by various category.

In `config.py`, you can cusomize your playlist.

If you need a playlist of 25 songs with your Top Artist of recent times

```python
CATEGORY = TopArtist(time_range=TimeRange.short_term, no_of_tracks_required=25) 
```

Like this you can use

- `TopArtist()`
- `TopTracks()`
- `TopMix()` - It mix both TopArtist and TopTracks
- `RecentlyPlayed()`

If you need a playlist with particualar artists, tracks or genre, you can use `Mix()`
In Mix you can mix upto 5 parameter like Artist, Genre and Track. Only 5 parameter are allowed

```python
CATEGORY = Mix(
    [
        Artist("7jVv8c5Fj3E9VhNjxT4snq"),
        Artist("6M2wZ9GZgrQXHCFfjv46we"),
        Artist("1Xyo4u8uXC1ZmMpatF05PJ"),
        Genre("pop"),
        Track("0HqZX76SFLDz2aW8aiqi7G")
    ]
)
```

## Contributions

Contributions are Welcome. Feel free to report bugs in issue and fix some bugs by creating pull requests. Comments, Suggestions, Improvements and Enhancements are always welcome.

## Contact

If you have any questions or feedback about this project, feel free to get in touch with me via [mail](yogeshin247@gmail.com)

Thank you;

Made with Music ❤️
