🎵 Spotify Mood Analysis Playlist Generator

A full-stack web application that turns your **feelings into playlists**.  
It uses **Natural Language Processing (NLP)** to analyze user input (mood, text, or keywords) and generates a personalized Spotify playlist that matches your vibe.

---

🚀 Features
- **Mood Detection**: Analyzes user text input to detect emotions
- **Spotify Integration**: Uses Spotify Web API to generate playlists
- **Full-Stack App**: Built with a React frontend and Python backend
- **Customizable Playlists**: Users can tweak genres, track count, and mood intensity
- **Secure Authentication**: OAuth-based login with Spotify

---

🛠️ Tech Stack
**Frontend:** React, JavaScript, CSS  
**Backend:** Python (Flask / FastAPI)  
**APIs:** Spotify Web API  
**NLP:** NLTK / TextBlob / spaCy  
**Auth:** Spotify OAuth 2.0

---

📂 Project Structure
```
SpotifyMoodAnalyzer/
│── backend/        # Python API for mood detection and Spotify requests
│── frontend/       # React UI for playlist generation
│── requirements.txt
│── package.json
│── README.md
```

---

⚡ Getting Started

1. Clone the Repository
```bash
git clone https://github.com/vrb17/Spotify-Mood-Analysis-Playlist-Generator.git
cd Spotify-Mood-Analysis-Playlist-Generator
```

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

3. Frontend Setup
```bash
cd frontend
npm install
npm start
```

4. Environment Variables
Create a `.env` file in both **frontend** and **backend**:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:3000/callback
```

---

🎯 Usage
1. Login with Spotify
2. Enter a mood, feeling, or short description
3. App generates a playlist matching your mood
4. Save it directly to your Spotify library

---

📜 License
This project is licensed under the **MIT License** - see the LICENSE file for details.

---

🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss what you’d like to change.

---

## 🌟 Acknowledgements
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [NLTK](https://www.nltk.org/)
- [React](https://react.dev/)
