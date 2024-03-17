"""
Script to retrieve recent favorite artist and track data from Spotify API.
- Spotify docs : https://developer.spotify.com/
"""
import os
import logging
import json
from pathlib import Path

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv


OUTPUT_FILE_PATH = 'spotify_data.json'
LOG_PATH = "logs/spotify_data_retrieval.log"
ENV_VAR = load_dotenv()


# Set up logs for script
Path("./logs").mkdir(parents=True, exist_ok=True)
logger = logging.getLogger(__name__)
logging.basicConfig(
    filename=LOG_PATH, encoding="utf-8", level=logging.INFO
)

try:
    sp = Spotify(
        auth_manager=SpotifyOAuth(
            scope="user-top-read",
            client_id=os.environ["SPOTIFY_CLIENT_ID"],
            client_secret=os.environ["SPOTIFY_CLIENT_SECRET"],
            # Passing localhost as redirect_uri as it's not a mission critical feature
            redirect_uri="http://localhost/",
        )
    )
    spotify_recent_tracks_resp = sp.current_user_top_tracks(
        limit=5, time_range="short_term"
    )
    spotify_recent_artists_resp = sp.current_user_top_artists(
        limit=5, time_range="short_term"
    )

# We don't really need to do anything special here. If the script fails, we just want to log it and make sure that the existing data isn't overwritten.
except Exception as e:
    logging.error(e)
    raise e

tracks = []
for i, item in enumerate(spotify_recent_tracks_resp["items"]):
    tracks.append(
        {
            "track_name": item["name"],
            "artist_name": item["album"].get("artists")[0].get("name"),
        }
    )

artists = []
for i, item in enumerate(spotify_recent_artists_resp["items"]):
    artists.append({i: item["name"]})

spotify_data = {"tracks": tracks,
                "artists": artists}

with open(OUTPUT_FILE_PATH, 'w', encoding='utf-8') as f:
    json.dump(spotify_data, f, ensure_ascii=False, indent=4)
