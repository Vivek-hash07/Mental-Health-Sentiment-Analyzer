import os
import pandas as pd
from datetime import datetime

# ✅ Centralized path for mood tracking logs
csv_file = "data/mood_tracker_logs.csv"

# Function to log mood
def log_mood(mood, emotion, message):
    # Create the data directory if it doesn't exist
    os.makedirs(os.path.dirname(csv_file), exist_ok=True)

    # Create a new entry
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "mood": mood,
        "emotion": emotion,
        "message": message
    }

    # Convert to DataFrame
    df = pd.DataFrame([entry])

    # Append to CSV
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, mode='w', header=True, index=False)

# Function to load mood logs
def load_mood_logs():
    if os.path.exists(csv_file):
        return pd.read_csv(csv_file)
    else:
        return pd.DataFrame(columns=["timestamp", "mood", "emotion", "message"])
