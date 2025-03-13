import streamlit as st
import pandas as pd
import os
from mood_tracker.mood_utils import log_mood
from datetime import datetime, timedelta
import altair as alt

# Set page config
st.set_page_config(page_title="Mood Tracker", page_icon="📊", layout="wide")

# Mood options
moods = ["Happy", "Sad", "Angry", "Neutral", "Anxious", "Excited", "Tired"]

# --- Tracker UI ---
st.title("📊 Mood Tracker")

st.markdown("Log your current mood and thoughts below:")

# Mood selector
selected_mood = st.selectbox("How are you feeling right now?", moods)

# Emotion text input
emotion_text = st.text_input("Describe your emotion in a word (e.g., calm, nervous):")

# Optional message input
message = st.text_area("Add an optional message (what's on your mind?)")

# Log mood button
if st.button("Log Mood"):
    if emotion_text.strip() == "":
        st.warning("Please enter at least an emotion word to log your mood.")
    else:
        log_mood(selected_mood, emotion_text, message)
        st.success("✅ Your mood has been logged successfully!")

# --- Mood Log History ---
st.markdown("---")
st.subheader("📘 Mood Log History")

log_path = "data/mood_tracker_logs.csv"

# Load mood logs
if os.path.exists(log_path):
    df = pd.read_csv(log_path)

    if not df.empty:
        st.dataframe(df[::-1], use_container_width=True)

        # --- Mood Distribution Chart ---
        st.subheader("📈 Mood Distribution")
        mood_counts = df["mood"].value_counts().reset_index()
        mood_counts.columns = ["Mood", "Count"]

        bar_chart = alt.Chart(mood_counts).mark_bar(color="#4B8BBE").encode(
            x=alt.X("Mood", sort='-y'),
            y="Count"
        ).properties(width=600, height=350)

        st.altair_chart(bar_chart)

        # --- Emotion Trend Over Time ---
        st.subheader("📉 Emotion Trend Over Time")

        df["timestamp"] = pd.to_datetime(df["timestamp"])
        emotion_counts = df.groupby([df["timestamp"].dt.date, "mood"]).size().reset_index(name="Count")

        line_chart = alt.Chart(emotion_counts).mark_line(point=True).encode(
            x="timestamp:T",
            y="Count:Q",
            color="mood:N"
        ).properties(width=700, height=350)

        st.altair_chart(line_chart)

        # --- Weekly Mood Summary ---
        st.markdown("---")
        st.subheader("🧾 Weekly Mood Summary")

        one_week_ago = datetime.now() - timedelta(days=7)
        weekly_logs = df[df["timestamp"] >= one_week_ago]

        if not weekly_logs.empty:
            mood_counts = weekly_logs["mood"].value_counts()
            most_common_mood = mood_counts.idxmax()
            mood_summary = "\n".join([f"• {mood}: {count} times" for mood, count in mood_counts.items()])

            st.markdown(f"### 🗓️ Past 7 Days Summary")
            st.markdown(f"**Most Common Mood:** {most_common_mood}")
            st.markdown(f"**Mood Frequencies:**\n{mood_summary}")

            # Supportive message
            insights = {
                "Happy": "You're doing great! Keep surrounding yourself with positivity. 😊",
                "Sad": "Consider some self-care or talking to someone. You're not alone. 💙",
                "Angry": "Try relaxing activities or journaling to release anger. 🧘",
                "Neutral": "A stable week! Try to explore more things you enjoy. 🌈",
                "Anxious": "Breathe deeply. You might benefit from mindfulness techniques. 🧠",
                "Excited": "Awesome! Keep riding that wave of enthusiasm! 🚀",
                "Tired": "Rest is important. Take breaks and care for your body. 😴"
            }

            st.info(insights.get(most_common_mood, "Stay strong and take care of yourself. 💪"))
        else:
            st.info("No mood data in the past 7 days to summarize.")
    else:
        st.info("No mood logs yet.")
else:
    st.info("No mood log file found.")
