# tracker.py

import streamlit as st
import pandas as pd
from datetime import datetime
import os
import altair as alt

# --- Constants ---
MOOD_LOG_PATH = "mood_logs.csv"
MOOD_OPTIONS = ["Positive", "Negative", "Neutral"]

# --- Utility: Save Mood Entry ---
def log_mood(emotion, notes=""):
    entry = {
        "Date": datetime.now().strftime("%Y-%m-%d"),
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Emotion": emotion,
        "Notes": notes
    }
    df = pd.DataFrame([entry])

    if os.path.exists(MOOD_LOG_PATH):
        df.to_csv(MOOD_LOG_PATH, mode='a', header=False, index=False)
    else:
        df.to_csv(MOOD_LOG_PATH, index=False)

# --- Utility: Load Mood Logs ---
def load_logs():
    if os.path.exists(MOOD_LOG_PATH):
        return pd.read_csv(MOOD_LOG_PATH)
    else:
        return pd.DataFrame(columns=["Date", "Time", "Emotion", "Notes"])


# --- Streamlit App ---
st.set_page_config(page_title="Mood Tracker", layout="wide")
st.title("📆 Mood Tracker")
st.markdown("Log your daily emotions and track your mental well-being over time.")

# --- Mood Logging ---
st.subheader("✍️ Log your current emotion")
col1, col2 = st.columns([1, 3])

with col1:
    mood = st.selectbox("Select how you feel:", MOOD_OPTIONS)
with col2:
    notes = st.text_input("Optional notes")

if st.button("📝 Submit Entry"):
    log_mood(mood, notes)
    st.success("Mood entry logged successfully!")

# --- View Mood History ---
st.subheader("📈 Mood History")
logs = load_logs()

if logs.empty:
    st.warning("No mood entries yet.")
else:
    st.dataframe(logs[::-1], use_container_width=True)

    # --- Mood Count Bar Chart ---
    st.markdown("### 🔢 Mood Frequency Chart")
    chart_data = logs["Emotion"].value_counts().reset_index()
    chart_data.columns = ["Emotion", "Count"]

    chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X('Emotion', sort=["Positive", "Neutral", "Negative"]),
        y='Count',
        color='Emotion',
        tooltip=['Emotion', 'Count']
    ).properties(height=400)

    st.altair_chart(chart, use_container_width=True)
