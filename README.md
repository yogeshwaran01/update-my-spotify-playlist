# update-my-spotify-playlist

Spotify Action is a simple GitHub actions to update Spotify playlist with new songs based on your top artists and recently played tracks.

## Setup

1. Fork this repo
2. Clone your repo in local
3. copy `.env-template` into `.env`
4. Install all Python requirements in `requirements.txt`
5. Go to the Spotify Developer Dashboard and log in with your Spotify account.
6. Click on the "Create an App" button and fill out the necessary information, such as the name and description of your application. Use `http://localhost:5000` as redirect URL
7. Once you've created the app, you'll be taken to the app dashboard. Here, you'll find your client ID, client secret and Redirect URL. Copy this and paste it your `.env` file
8. Create new playlist in your Spotify Account and copy the playlist id from the url. Paste the playlist id in `.env` file.
9. Run this Script `get_refresh_token.py` to get refresh token. Follow the instruction in this script. Copy the refresh token into `.env` file.
10. Run this Script `update.py` to update your Playlist
11. Commit changes if any. Don't commit `.env`
12. Add all env variable `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI`, `REFRESH_TOKEN`, `PLAYLIST_ID` in github repository secret. Checkout this [link](https://docs.github.com/en/actions/reference/encrypted-secrets) to add a new repository secret.
13. By default it updates daily at `2:47 UTC`. You can also change this by changing the cron in `/.github/workflows/main.yml` by using [Cron Generator](https://crontab.guru/).
