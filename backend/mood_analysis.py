from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

def analyze_mood(user_text):
    sia = SentimentIntensityAnalyzer()
    scores = sia.polarity_scores(user_text)

    valence = scores['compound']

    # Simple mapping logic (you can improve later)
    if valence >= 0.5:
        mood = {"valence": 0.9, "energy": 0.8}
    elif valence >= 0:
        mood = {"valence": 0.6, "energy": 0.5}
    else:
        mood = {"valence": 0.3, "energy": 0.4}

    return mood

