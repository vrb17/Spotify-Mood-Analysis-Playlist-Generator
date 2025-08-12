from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from mood_analysis import analyze_mood
from spotify_api import get_recommendations

# ─── load our .env variables ─────────────────────────────────────────────────
load_dotenv()

app = Flask(__name__)
# only allow our React dev server
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route("/")
def index():
    return "Spotify Mood Analyzer Backend is running."


@app.route("/generate-playlist", methods=["POST"])
def generate_playlist():
    data = request.get_json() or {}
    user_text = data.get("text", "")
    # figure out valence/energy from the user text
    mood = analyze_mood(user_text)
    # hit Spotify recommendations endpoint via client-credentials
    playlist = get_recommendations(mood)
    return jsonify(playlist)


if __name__ == "__main__":
    # plain HTTP on 5001, no SSL context needed
    app.run(debug=True, port=5001)


# from flask import Flask, request, jsonify, redirect
# from flask_cors import CORS
# import os
# import spotipy
# from mood_analysis import analyze_mood
# from spotify_api import get_recommendations
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

# # Load credentials from .env
# SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
# SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

# scope = "user-read-private"


# @app.route("/")
# def index():
#     return "Spotify Mood Analyzer Backend is running."


# @app.route("/generate-playlist", methods=["POST"])
# def generate_playlist():
#     data = request.get_json()
#     user_text = data.get("text")

#     mood = analyze_mood(user_text)
#     recommendations = get_recommendations(mood)

#     return jsonify(recommendations)


# if __name__ == "__main__":
#     app.run(ssl_context=('ssl/cert.pem', 'ssl/key.pem'), debug=True, port=5001)

