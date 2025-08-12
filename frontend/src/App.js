import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState("");
  const [playlist, setPlaylist] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

    const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);
    setError("");

    try {
      const { data } = await axios.post(
        "http://localhost:5001/generate-playlist",
        { text }
      );
      setPlaylist(data);
    } catch (err) {
      console.error(err);
      setError("Error generating playlist. Please make sure your backend is running.");
    }

    setLoading(false);
  };

  

  return (
    <div className="App">
      <h1>Spotify Mood Analyzer 🎵</h1>

      <form onSubmit={handleSubmit}>
        <textarea 
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="How are you feeling today?"
          rows={4}
          cols={50}
        />
        <br />
        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Generate Playlist"}
        </button>
      </form>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {playlist.length > 0 && (
        <div>
          <h2>Here’s your mood-based playlist:</h2>
          <ul>
            {playlist.map((track, index) => (
              <li key={index}>
                <a href={track.url} target="_blank" rel="noopener noreferrer">
                  {track.name} — {track.artist}
                </a>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
