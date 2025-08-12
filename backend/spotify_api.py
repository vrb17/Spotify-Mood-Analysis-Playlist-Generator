import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

# Initialize Spotipy client
def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
    ))

def print_available_genres():
    sp = get_spotify_client()
    try:
        genres = sp.recommendation_genre_seeds()
        print("✅ Available Spotify Genres:", genres)
    except Exception as e:
        print("❌ Error fetching genre seeds:", e)

# 🔎 Optional: Uncomment to inspect available genres
# print_available_genres()

def get_recommendations(mood):
    sp = get_spotify_client()
    try:
        # Choose one of these valid genre seeds after printing available genres
        seed_genres = ["pop", "rock", "chill", "hip-hop", "edm"]

        results = sp.recommendations(
            seed_genres=[seed_genres[0]],  # or pick one based on mood
            limit=10,
            target_valence=mood["valence"],
            target_energy=mood["energy"]
        )

        playlist = []
        for track in results["tracks"]:
            playlist.append({
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "url": track["external_urls"]["spotify"]
            })

        return playlist

    except Exception as e:
        print("Error fetching recommendations:", e)
        return []
